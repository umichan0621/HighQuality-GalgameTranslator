from function.word_counter import WordCounter
from function.excel_parser import ExcelParser


excel_parser=ExcelParser()
#打开excel路径
excel_parser.SetExcelPath("dictionary.xlsx")
#遍历已记录的词，加入集合
word_set=excel_parser.GetWordSet()

word_counter=WordCounter()
#设置文件编码格式
word_counter.SetEncodingMethod("utf-16le")
#打开需要统计的文件路径
word_counter.SetFilePath("example.txt")
#使用记录词的集合，避免重复统计
word_counter.SetWordSet(word_set)
#解析
word_counter.ParseText()
#按词频排序输出
word_map=word_counter.SortNewDict()
for word in word_map:
    print(word[0],word[1])

