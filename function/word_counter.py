import MeCab

class WordCounter:
    file_path=""
    encoding_method="utf-16le"
    word_set=set()#保存已记录的词
    word_dict={}#统计未记录的词
    
    def SetFilePath(self,file_path):
        self.file_path=file_path
    
    def SetEncodingMethod(self,encoding_method):
        self.encoding_method=encoding_method
    
    def SetWordSet(self,word_set):
        self.word_set=word_set

    def __GetWords(self,text):
        wakati = MeCab.Tagger("-Owakati")
        res=wakati.parse(text).split()
        return res

    def __HandleWord(self,word):
        if len(word)>1:
            if word not in self.word_set:
                if word in self.word_dict:
                    self.word_dict[word]+=1
                else:
                    self.word_dict[word]=1

    def ParseText(self):
        with open(self.file_path,'r',encoding=self.encoding_method) as source_file:
            for text in source_file:
                if(text[0]!='{'):
                    text=text.replace("\\n","")
                    text=text.replace("…"," ")
                    text=text.replace("。"," ")
                    text=text.replace("！"," ")
                    text=text.replace("？"," ")
                    text=text.replace("、"," ")
                    text=text.replace("\"","")
                    text=text.replace("「","")
                    text=text.replace("」","")
                    word_arr=self.__GetWords(text)
                    for word in word_arr:
                        self.__HandleWord(word)
    
    def SortNewDict(self):
        self.word_dict=sorted(self.word_dict.items(),key=lambda x:x[1],reverse=True)
        return self.word_dict
