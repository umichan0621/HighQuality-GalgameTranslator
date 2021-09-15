from function.excel_parser import ExcelParser
from function.general_text_processor import GeneralTextProcessor
from machine_translator.tencent_translator import TencentMachineTranslator
import time

excel_parser = ExcelParser()
excel_parser.SetExcelPath("E:\HighQuality-GalgameTranslator\dictionary.xlsx")
word_map = excel_parser.GetWordMap()
general_text_processor = GeneralTextProcessor()
general_text_processor.SetWordMap(word_map)
tencent_machine_translator = TencentMachineTranslator()

api_id = "AKIDxfT4wa1o30hjjL9yn10hILr1vc4GDEzI"
api_key = "sNefQvORi6FryXqC3gphinFFzrLAVNK0"
tencent_machine_translator.SetIdAndKey(api_id, api_key)


# 针对不同游戏做特殊处理
def ModifySourceSpecialText(text):
    res = text
    res = res.replace('\\n', '←')  # 删除翻译文本的换行符
    res = res.replace('\n', '')  # 删除文本换行的换行符
    res = res.replace('\A', 'AX-01')  # 暂时替换主角名字为A
    res = res.replace('\\s', '')  # 删除字体变小占位符
    res = res.replace('\\b', '')  # 暂时替换加粗占位符为箭头
    res = res.replace('\\B', '')  # 删掉部分加粗
    res = res.replace('<color ff00ff>', '')  # 颜色
    res = res.replace('</color>', '')  # 颜色
    return res


# 针对不同游戏做特殊处理的复原
def RecoverTransSpecialText(source_text, target_text):
    res = target_text
    res = res.replace('←', '\\n')
    res = res.replace('AX-01', '\A')  # 恢复主角名字为占位符
    res = res.replace('“”', '”')  # 替换有问题的引号
    res = res.replace('……。', '……')  # 替换有问题的省略号
    # 恢复颜色
    if source_text.find("<color") != -1:
        res = "<color ff00ff>" + res + "</color>"
    # 恢复加粗
    if source_text.find("\\b") != -1:
        res = "\\b" + res
    # 恢复小号字体
    if source_text.find("\\s") != -1:
        res = "\\s" + res
    return res


class BishopTranslator:
    __source_file_content = 0  # 读取原文并保存为数组
    __output_file = 0  # 输出文件
    __total_line = 0
    __cur_line = 0

    def SetSourceTextPath(self, file_path):
        # 读取原文并保存为数组
        source_file = open(file_path, 'r', encoding="utf-16le")
        self.__source_file_content = source_file.readlines()
        self.__total_line = len(self.__source_file_content)
        # 打开译文文件，位置在原文文件路径下，后缀_zh
        target_path = file_path.replace(".txt", "_zh.txt")
        self.__output_file = open(target_path, 'a+', encoding="utf-16le")
        self.__output_file.write("")
        # 读取译文文件行数
        self.__cur_line = len(open(target_path, 'r', encoding="utf-16le").readlines())

    def TranslateSourceText(self):
        while self.__cur_line < self.__total_line:
            self.__HandleText()
            time.sleep(0.1)

    def __HandleText(self):
        source_text = self.__source_file_content[self.__cur_line]
        # 偶数行是标记行
        if self.__cur_line % 2 == 0:
            self.__output_file.write(source_text.replace('0}', '1}'))
        # 奇数行是原文文本
        else:
            self.__HandleSourceText(source_text)
        self.__cur_line += 1

    def __HandleSourceText(self, source_text):
        # 文本特殊处理
        res = ModifySourceSpecialText(source_text)
        # 文本通用处理
        res = general_text_processor.ModifySourceText(res)
        # 机器翻译文本
        res = tencent_machine_translator.Translate(res)
        # 复原通用处理
        res = general_text_processor.RecoverTransText(res)
        # 复原特殊处理
        res = RecoverTransSpecialText(source_text, res)
        print(res)
        # print("----------------------")
        self.__output_file.write(res + '\n')
        # res = res.replace('\n', '')  # 删除文本换行的换行符


B = BishopTranslator()
B.SetSourceTextPath("../example.txt")
B.TranslateSourceText()
