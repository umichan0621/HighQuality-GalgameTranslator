import random


def GenRandomStr():
    res = random.choice('UXYZ')
    res += random.choice('CRFGHIJKLMNQRSUW')
    res += '-'
    res += random.choice('1234567890')
    res += random.choice('1234567890')
    return res


# 处理文本中在通用词表内的词语
class GeneralTextProcessor:
    word_map = {}
    src_to_temp = {}  # {原文:中间替代}
    temp_to_des = {}  # {中间替代:翻译}
    des_to_temp = {}  # {翻译:中间替代}

    # 载入字典，生成替换词表
    def SetWordMap(self, word_map):
        self.word_map = word_map
        for word in self.word_map:
            src = word
            des = self.word_map[word]
            # 不同原文同翻译
            if des in self.des_to_temp.keys():
                self.src_to_temp[src] = self.des_to_temp[des]
            else:
                temp = GenRandomStr()
                # 随机生成中间替换词（例如：AB-21），生成直到不重复
                while 1:
                    if temp in self.temp_to_des.keys():
                        temp = GenRandomStr()
                    else:
                        break
                self.src_to_temp[src] = temp
                self.temp_to_des[temp] = des
                self.des_to_temp[des] = temp

    # 替换原文中在字典内的词语
    def ModifySourceText(self, text):
        res = text
        for i in self.src_to_temp:  # 字典替换
            res = res.replace(i, self.src_to_temp[i])
        return res

    # 恢复译文中替换的词语
    def RecoverTransText(self, text):
        res = text
        for i in self.temp_to_des:
            res = res.replace(i, self.temp_to_des[i])
        return res
