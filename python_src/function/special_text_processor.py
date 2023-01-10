class SpecialTextProcessor:
    handle_step1 = {}
    handle_step2 = {}
    handle_step3 = {}

    def SetSpecialWordMap(self, handle_step1, handle_step2, handle_step3):
        self.handle_step1 = handle_step1
        self.handle_step2 = handle_step2
        self.handle_step3 = handle_step3

    # 针对不同游戏做特殊处理
    def ModifySourceSpecialText(self, des_text):
        res = des_text
        res = res.replace('\n', '')
        # 特殊处理第一阶段
        for src in self.handle_step1:
            des = self.handle_step1[src]
            res = res.replace(src, des)
        return res

    # 针对不同游戏做特殊处理的复原
    def RecoverTransSpecialText(self, src_text, des_text):
        res = des_text
        # 特殊处理第二阶段
        for src in self.handle_step2:
            des = self.handle_step2[src]
            res = res.replace(src, des)
        for src in self.handle_step3:
            des = self.handle_step3[src]
            if src_text.find(src) != -1:
                res = des[0]+res+des[1]
        return res
