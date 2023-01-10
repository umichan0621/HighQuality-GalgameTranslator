from PyQt5.Qt import QThread, pyqtSignal
from function.word_counter import WordCounter
from function.excel_parser import ExcelParser


class BishopCounter(QThread):
    print_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.excel_parser = ExcelParser()
        self.word_counter = WordCounter()
        self.__src_text_path = ""

    def Init(self, word_dic_path, src_text_path):
        if len(word_dic_path) <= 5 or word_dic_path[len(word_dic_path) - 5:len(word_dic_path)] != ".xlsx":
            self.print_signal.emit("词表路径错误")
            return
        if len(src_text_path) <= 4 or src_text_path[len(src_text_path) - 4:len(src_text_path)] != ".txt":
            self.print_signal.emit("原文文件路径错误")
            return
        self.excel_parser.SetExcelPath(word_dic_path)
        self.__src_text_path = src_text_path

    def run(self):
        self.print_signal.emit("开始读取词表...")
        # 遍历已记录的词，加入集合
        word_set = set()
        self.excel_parser.GetWordSet(word_set)
        # 使用记录词的集合，避免重复统计
        self.word_counter.SetWordSet(word_set)
        self.print_signal.emit("成功载入词表")
        self.print_signal.emit("开始读取原文文件...")
        source_file = open(self.__src_text_path, 'r', encoding="utf-16le")
        source_file_content = source_file.readlines()
        self.print_signal.emit("成功读取原文文件")
        self.print_signal.emit("开始统计，耗时很久，请不要关闭")
        for src_text in source_file_content:
            src_text = src_text.replace('\n', '')
            if src_text.count('{') == 0:
                self.word_counter.HandleText(src_text)
        word_map = self.word_counter.SortNewDict()
        for word in word_map:
            self.print_signal.emit(word[0] + " " + str(word[1]))

