import xlrd


class ExcelParser:
    file_path = ""
    word_set = set()
    word_map = {}

    def SetExcelPath(self, file_path):
        self.file_path = file_path

    # 载入已记录的词语
    def GetWordSet(self):
        book = xlrd.open_workbook(self.file_path)
        for sheet in book.sheets():
            sheet = book.sheet_by_name(sheet.name)
            for i in range(sheet.nrows):
                if i != 0:
                    self.word_set.add(sheet.row_values(i)[0])
        return self.word_set

    # 载入词表
    def GetWordMap(self):
        book = xlrd.open_workbook(self.file_path)
        for sheet in book.sheets():
            sheet = book.sheet_by_name(sheet.name)
            # 忽略过滤表
            if sheet.name != "过滤":
                for i in range(sheet.nrows):
                    if i != 0:
                        if len(sheet.row_values(i)[1]) > 0:
                            self.word_map[sheet.row_values(i)[0]] = sheet.row_values(i)[1]
        return self.word_map
