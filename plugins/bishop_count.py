from function.word_counter import WordCounter
from function.excel_parser import ExcelParser


class BishopCounter:
    __word_counter = 0
    __excel_parser = 0

    def SetDicPath(self, dic_path):
        self.__excel_parser = ExcelParser()
        # 打开excel路径
        self.__excel_parser.SetExcelPath(dic_path)
        # 遍历已记录的词，加入集合
        word_set = set()
        self.__excel_parser.GetWordSet(word_set)
        self.__word_counter = WordCounter()
        # 使用记录词的集合，避免重复统计
        self.__word_counter.SetWordSet(word_set)

    def ParseSrcFile(self, file_path):
        source_file = open(file_path, 'r', encoding="utf-16le")
        source_file_content = source_file.readlines()
        for src_text in source_file_content:
            src_text = src_text.replace('\n', '')
            if src_text.count('{') == 0:
                self.__word_counter.HandleText(src_text)

    def GetWordCount(self):
        return self.__word_counter.SortNewDict()
