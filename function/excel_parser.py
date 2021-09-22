import xlrd


class ExcelParser:
    file_path = ""

    def SetExcelPath(self, file_path):
        self.file_path = file_path

    # 载入已记录的词语
    def GetWordSet(self, word_set):
        book = xlrd.open_workbook(self.file_path)
        for sheet in book.sheets():
            sheet = book.sheet_by_name(sheet.name)
            for i in range(sheet.nrows):
                if i != 0:
                    word_set.add(sheet.row_values(i)[0])

    # 载入通用词表和特殊词表
    def GetWordMap(self, word_map):
        book = xlrd.open_workbook(self.file_path)
        for sheet in book.sheets():
            sheet = book.sheet_by_name(sheet.name)
            # 忽略过滤表
            if sheet.name == "通用词表" or sheet.name == "特殊词表":
                for i in range(sheet.nrows):
                    if i != 0 and len(sheet.row_values(i)[0]) > 0 and len(sheet.row_values(i)[1]) > 0:
                        src_text = sheet.row_values(i)[0]
                        des_text = sheet.row_values(i)[1]
                        word_map[src_text] = des_text

    # 载入特殊处理词表
    def GetSpecialWordMap(self, handle_step1, handle_step2, handle_step3):
        book = xlrd.open_workbook(self.file_path)
        for sheet in book.sheets():
            sheet = book.sheet_by_name(sheet.name)
            if sheet.name == "特殊处理":
                for i in range(sheet.nrows):
                    if i != 0 and len(sheet.row_values(i)[0]) > 0:
                        key_word = sheet.row_values(i)[0]
                        handle1 = sheet.row_values(i)[1]
                        handle2 = sheet.row_values(i)[2]
                        seq = sheet.row_values(i)[3]
                        seq = (seq-seq % 10000)/10000
                        if seq == 1:
                            handle_step1[key_word] = handle1
                        elif seq == 2:
                            handle_step2[key_word] = handle1
                        elif seq == 3:
                            handle_step3[key_word] = [handle1, handle2]
