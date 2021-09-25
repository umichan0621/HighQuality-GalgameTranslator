import time
from PyQt5.Qt import QThread, pyqtSignal
from function.excel_parser import ExcelParser
from function.general_text_processor import GeneralTextProcessor
from function.special_text_processor import SpecialTextProcessor
from machine_translator.general_translator import GeneralTranslator


class BishopTranslator(QThread):
    print_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__general_machine_translator = GeneralTranslator()
        self.__general_text_processor = GeneralTextProcessor()
        self.__special_text_processor = SpecialTextProcessor()
        self.__word_dic_path = ""
        self.__src_text_path = ""
        self.__source_file_content = []  # 读取原文并保存为数组
        self.__output_file = 0  # 输出文件
        self.__total_line = 0
        self.__cur_line = 0

    def Init(self, word_dic_path, src_text_path, api_id, api_key):
        if len(word_dic_path) <= 5 or word_dic_path[len(word_dic_path) - 5:len(word_dic_path)] != ".xlsx":
            self.print_signal.emit("词表路径错误")
            return
        if len(src_text_path) <= 4 or src_text_path[len(src_text_path) - 4:len(src_text_path)] != ".txt":
            self.print_signal.emit("原文文件路径错误")
            return
        self.__general_machine_translator.SetApiIdAndKey(api_id, api_key)
        self.__word_dic_path = word_dic_path
        self.__src_text_path = src_text_path

    def __LoadWordDic(self):
        excel_parser = ExcelParser()
        excel_parser.SetExcelPath(self.__word_dic_path)
        # 读取通用词表和特殊词表
        word_map = {}
        excel_parser.GetWordMap(word_map)
        self.__general_text_processor.SetWordMap(word_map)
        # 读取特殊处理词表
        handle_step1 = {}
        handle_step2 = {}
        handle_step3 = {}
        excel_parser.GetSpecialWordMap(handle_step1, handle_step2, handle_step3)
        self.__special_text_processor.SetSpecialWordMap(handle_step1, handle_step2, handle_step3)

    def __LoadTxtFile(self):
        # 读取原文并保存为数组
        source_file = open(self.__src_text_path, 'r', encoding="utf-16le")
        self.__source_file_content = source_file.readlines()
        self.__total_line = len(self.__source_file_content)
        # 打开译文文件，位置在原文文件路径下，后缀_zh
        target_path = self.__src_text_path.replace(".txt", "_zh.txt")
        self.__output_file = open(target_path, 'a+', encoding="utf-16le")
        self.__output_file.write("")
        # 读取译文文件行数
        self.__cur_line = len(open(target_path, 'r', encoding="utf-16le").readlines())

    def __HandleText(self):
        source_text = self.__source_file_content[self.__cur_line]
        # 偶数行是标记行
        if self.__cur_line % 2 == 0:
            self.__output_file.write(source_text.replace('0}', '1}'))
            self.__cur_line += 1
            return [source_text]
        # 奇数行是原文文本
        else:
            res = self.__HandleSourceText(source_text)
            self.__cur_line += 1
            return [source_text, res]

    def __HandleSourceText(self, source_text):
        # 文本特殊处理
        res = self.__special_text_processor.ModifySourceSpecialText(source_text)
        # 文本通用处理
        res = self.__general_text_processor.ModifySourceText(res)
        # 机器翻译文本
        res = self.__general_machine_translator.Translate(res)
        if res == "ERROR":
            return "ERROR"
        # 复原通用处理
        res = self.__general_text_processor.RecoverTransText(res)
        # 复原特殊处理
        res = self.__special_text_processor.RecoverTransSpecialText(source_text, res)
        self.__output_file.write(res + '\n')
        return res

    def run(self):
        self.print_signal.emit("开始读取词表...")
        self.__LoadWordDic()
        self.__LoadTxtFile()
        self.print_signal.emit("开始Bishop机器翻译...")
        while self.__cur_line < self.__total_line:
            res = self.__HandleText()
            if len(res) == 2:
                # 机器翻译API发生错误
                if res[1] == "ERROR":
                    self.print_signal.emit("机器翻译API发生错误，请检查API的ID和Key是否正确")
                    return
                self.print_signal.emit(res[0].replace("\n", "")+'\n'+res[1]+'\n')
            else:
                self.print_signal.emit("Address:"+res[0][11:18])
            time.sleep(0.1)
        self.print_signal.emit("Bishop机器翻译完成")
