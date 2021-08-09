from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.tmt.v20180321 import tmt_client, models
import json
import random
import time
from function.excel_parser import ExcelParser

class MachineTranslator:
    client=0
    req=0
    def SetIdAndKey(self,api_id,api_key):
        cred = credential.Credential(api_id,api_key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.client = tmt_client.TmtClient(cred, "ap-shanghai", clientProfile) 
        self.req = models.TextTranslateRequest()

    def Translate(self,source_text):
        params = '{\"SourceText\":\"'+source_text+'\",\"Source\":\"ja\",\"Target\":\"zh\",\"ProjectId\":0}'
        self.req.from_json_string(params)
        resp = self.client.TextTranslate(self.req)
        dic=json.loads(resp.to_json_string())
        return dic["TargetText"]

class TextProcessor:
    word_map={}
    src_to_temp={}#{原文:中间替代}
    temp_to_des={}#{中间替代:翻译}
    des_to_temp={}#{翻译:中间替代}

    def SetWordMap(self,word_map):
        self.word_map=word_map
        self.__GenDictionary()


    def __GenRandomStr(self): 
        res=random.choice('CDRFGHIJKLMNOPQRSUVWXYZ')
        res+=random.choice('CDRFGHIJKLMNOPQRSUVWXYZ')
        res+='-'
        res+=random.choice('1234567890')
        res+=random.choice('1234567890')
        return res

    def __GenDictionary(self):
        for word in self.word_map:
            src=word
            des=self.word_map[word]
            #不同原文同翻译
            if des in self.des_to_temp.keys():
                
                self.src_to_temp[src]=self.des_to_temp[des]
            else:
                temp=self.__GenRandomStr()
                while(1):
                    if temp in self.temp_to_des.keys():
                        temp=self.__GenRandomStr()
                    else:
                        break
                self.src_to_temp[src]=temp
                self.temp_to_des[temp]=des
                self.des_to_temp[des]=temp
    
    def ModifySourceText(self,text):
        res=text
        res=res.replace('\\n','←')          #删除翻译文本的换行符
        res=res.replace('\n','')            #删除文本换行的换行符
        res=res.replace('\A','AX-01')       #暂时替换主角名字为A
        res=res.replace('\\s','')           #删除字体变小占位符
        res=res.replace('\\b','')           #暂时替换加粗占位符为箭头
        res=res.replace('\\B','')           #删掉部分加粗
        res=res.replace('<color ff00ff>','')#颜色
        res=res.replace('</color>','')      #颜色
        for i in self.src_to_temp:          #字典替换
            res=res.replace(i,self.src_to_temp[i])
        return res

    def RecoverTransText(self,text):
        res=text
        for i in self.temp_to_des:
            res=res.replace(i,self.temp_to_des[i])  
        res=res.replace('←','\\n') 
        res=res.replace('AX-01','\A')   #恢复主角名字为占位符
        res=res.replace('“”','”')       #替换有问题的引号
        res=res.replace('……。','……')    #替换有问题的省略号
        return res

class TextTranslator:
    excel_parser=0
    text_processor=0
    machine_translator=0
    output_path=""
   
    def SetExcelPath(self,excel_path):
        self.excel_parser=ExcelParser()
        self.excel_parser.SetExcelPath(excel_path)
        self.text_processor=TextProcessor()
        word_map=self.excel_parser.GetWordMap()
        self.text_processor.SetWordMap(word_map)

    def SetOutputPath(self,file_path):
        self.output_path=file_path
    
    def SetIdAndKey(self,api_id,api_key):
        self.machine_translator=MachineTranslator()
        self.machine_translator.SetIdAndKey(api_id,api_key)

    def Parse(self,file_path,encoding_method):
        with open(file_path,'r',encoding=encoding_method) as source_file:
            counter=0
            for text in source_file:
                counter+=1
                res=''
                if counter%2==1:
                    res=text.replace('0}','1}')          
                else:
                    print(text)
                    res=self.text_processor.ModifySourceText(text)   #文本处理 
                    res=self.machine_translator.Translate(res)       #翻译文本 
                    res=self.text_processor.RecoverTransText(res)    #复原译文格式       
                    if text.find("<color")!=-1:
                        res="<color ff00ff>"+res+"</color>"
                    if text.find("\\b")!=-1:
                        res="\\b"+res
                    if text.find("\\s")!=-1:
                        res="\\s"+res
                    print(res)
                    print("----------------------")
                res=res.replace('\n','')            #删除文本换行的换行符
                with open(self.output_path,'a+',encoding='utf-16') as output_file:
                    output_file.write(res+'\n')
                time.sleep(0.1)
