import MeCab


def GetWords(text):
    wakati = MeCab.Tagger("-Owakati")
    res = wakati.parse(text).split()
    return res


# 统计文本中频繁出现的词语
class WordCounter:
    word_set = set()  # 保存已记录的词
    word_dict = {}  # 统计未记录的词

    def SetWordSet(self, word_set):
        self.word_set = word_set

    def __HandleWord(self, word):
        # 词语长度大于1且未收录入词表
        if len(word) > 1 and word not in self.word_set:
            # 之前已记录
            if word in self.word_dict:
                self.word_dict[word] += 1
            # 第一次遇到
            else:
                self.word_dict[word] = 1

    def HandleText(self, src_text):
        word_arr = GetWords(src_text)
        for word in word_arr:
            self.__HandleWord(word)

    def SortNewDict(self):
        self.word_dict = sorted(self.word_dict.items(), key=lambda x: x[1], reverse=True)
        return self.word_dict
