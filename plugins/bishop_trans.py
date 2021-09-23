from function.excel_parser import ExcelParser
from function.general_text_processor import GeneralTextProcessor
from function.special_text_processor import SpecialTextProcessor
from machine_translator.general_translator import GeneralTranslator


class BishopTranslator:
    __source_file_content = 0  # 读取原文并保存为数组
    __output_file = 0  # 输出文件
    __total_line = 0
    __cur_line = 0
    __general_text_processor = 0
    __special_text_processor = 0
    __general_machine_translator = 0

    def SetGeneralTrans(self, api_id, api_key):
        self.__general_machine_translator = GeneralTranslator()
        self.__general_machine_translator.SetApiIdAndKey(api_id, api_key)

    def SetWordDicPath(self, word_dic_path):
        excel_parser = ExcelParser()
        excel_parser.SetExcelPath(word_dic_path)
        # 读取通用词表和特殊词表
        word_map = {}
        excel_parser.GetWordMap(word_map)
        self.__general_text_processor = GeneralTextProcessor()
        self.__general_text_processor.SetWordMap(word_map)
        # 读取特殊处理词表
        handle_step1 = {}
        handle_step2 = {}
        handle_step3 = {}
        excel_parser.GetSpecialWordMap(handle_step1, handle_step2, handle_step3)
        self.__special_text_processor = SpecialTextProcessor()
        self.__special_text_processor.SetSpecialWordMap(handle_step1, handle_step2, handle_step3)

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

    def GetCurLine(self):
        return self.__cur_line

    def GetTotalLine(self):
        return self.__total_line

    def TranslateSourceText(self):
        while self.__cur_line < self.__total_line:
            self.HandleText()

    def HandleText(self):
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
        # res = res.replace('\n', '')  # 删除文本换行的换行符
        return res

