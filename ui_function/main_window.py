import sys
import time
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from ui_function.menu import Menu
from ui_function.setting import Setting
from ui_function.machine_trans import MachineTrans
from ui_function.word_count import WordCount
from plugins.bishop_trans import BishopTranslator
from plugins.bishop_count import BishopCounter


class MainWindow:
    # 0表示MachineTrans窗体，1表示WordCount窗体，2表示Setting窗体
    __static = -1
    __main_window = 0
    __menu = 0
    __setting = 0
    __machine_trans = 0
    __word_count = 0

    def Init(self):
        app = QApplication(sys.argv)
        self.__main_window = QWidget()
        self.__main_window.setWindowTitle("HighQuality-GalgameTranslator")
        self.__main_window.setFixedSize(960, 720)
        # 初始化菜单栏
        self.__menu = Menu()
        self.__menu.Init()
        self.__menu.GetMenuWidget().menuWidget.setParent(self.__main_window)
        # 初始化机器翻译窗体
        self.__machine_trans = MachineTrans()
        self.__machine_trans.Init()
        self.__machine_trans.GetMachineTransWidget().machineTransWidget.setParent(self.__main_window)
        # 初始化统计窗体
        self.__word_count = WordCount()
        self.__word_count.Init()
        self.__word_count.GetWordCountWidget().wordCountWidget.setParent(self.__main_window)
        # 初始化设置窗体
        self.__setting = Setting()
        self.__setting.Init()
        self.__setting.GetSettingWidget().settingWidget.setParent(self.__main_window)
        # 设置Menu窗体按钮的信号和槽
        self.__menu.GetMenuWidget().settingButton.clicked.connect(self.__ChangeToSetting)
        self.__menu.GetMenuWidget().machineTranslateButton.clicked.connect(self.__ChangeToMachineTrans)
        self.__menu.GetMenuWidget().wordCountButton.clicked.connect(self.__ChangeToWordCount)
        # 设置机器翻译开始翻译按钮的信号和槽
        self.__machine_trans.GetMachineTransWidget().startTransButton.clicked.connect(self.PluginBishopTrans)
        # 设置词频统计开始统计按钮的信号和槽
        self.__word_count.GetWordCountWidget().startCountButton.clicked.connect(self.PluginBishopCount)
        self.__ChangeToMachineTrans()
        # 启动主窗体
        self.__main_window.show()
        sys.exit(app.exec_())

    def __ChangeToMachineTrans(self):
        if self.__static == 0:
            return
        elif self.__static == 1:
            self.__word_count.Hide()
        elif self.__static == 2:
            self.__setting.Hide()
        self.__machine_trans.Show()
        self.__static = 0

    def __ChangeToWordCount(self):
        if self.__static == 1:
            return
        elif self.__static == 0:
            self.__machine_trans.Hide()
        elif self.__static == 2:
            self.__setting.Hide()
        self.__word_count.Show()
        self.__static = 1

    def __ChangeToSetting(self):
        if self.__static == 2:
            return
        # 当前是MachineTrans窗体
        elif self.__static == 0:
            print(1)
            self.__machine_trans.Hide()
        # 当前是WordCount窗体
        elif self.__static == 1:
            self.__word_count.Hide()
        self.__setting.Show()
        self.__static = 2

    def PluginBishopTrans(self):
        bishop_translator = BishopTranslator()
        # 读取原文路径
        src_text_path = self.__setting.GetSettingWidget().srcFilePathEdit.text().replace("\n", "")
        self.__machine_trans.Print("开始读取原文文件...")
        if len(src_text_path) > 4 and src_text_path[len(src_text_path) - 4:len(src_text_path)] == ".txt":
            bishop_translator.SetSourceTextPath(src_text_path)
            self.__machine_trans.Print("成功读取原文文件")
        else:
            print(src_text_path)
            self.__machine_trans.Print("原文文件路径错误")
            return
        # 读取词表路径
        word_dic_path = self.__setting.GetSettingWidget().wordsDicEdit.text().replace("\n", "")
        self.__machine_trans.Print("开始读取词表...")
        if len(word_dic_path) > 5 and word_dic_path[len(word_dic_path) - 5:len(word_dic_path)] == ".xlsx":
            bishop_translator.SetWordDicPath(word_dic_path)
            self.__machine_trans.Print("成功载入词表")
        else:
            self.__machine_trans.Print("词表路径错误")
            return
        self.__machine_trans.Print("开始读取翻译API的ID和Key...")
        api_id = self.__setting.GetSettingWidget().txAPIIDEdit.text().replace("\n", "")
        api_key = self.__setting.GetSettingWidget().txAPIKeyEdit.text().replace("\n", "")
        bishop_translator.SetGeneralTrans(api_id, api_key)
        self.__machine_trans.Print("开始Bishop机器翻译...")
        while bishop_translator.GetCurLine() < bishop_translator.GetTotalLine():
            res = bishop_translator.HandleText()
            if len(res) == 2:
                # 机器翻译API发生错误
                if res[1] == "ERROR":
                    self.__machine_trans.Print("机器翻译API发生错误，请检查API的ID和Key是否正确")
                    return
                self.__machine_trans.Print(res[0].replace("\n", ""))
                self.__machine_trans.Print(res[1])
                self.__machine_trans.Print("")
            else:
                self.__machine_trans.Print("Address:"+res[0][11:18])
            time.sleep(0.1)
        self.__machine_trans.Print("Bishop机器翻译完成")

    def PluginBishopCount(self):
        bishop_counter = BishopCounter()
        # 读取词表路径
        word_dic_path = self.__setting.GetSettingWidget().wordsDicEdit.text().replace("\n", "")
        self.__word_count.Print("开始读取词表...")
        if len(word_dic_path) > 5 and word_dic_path[len(word_dic_path) - 5:len(word_dic_path)] == ".xlsx":
            bishop_counter.SetDicPath(word_dic_path)
            self.__word_count.Print("成功载入词表")
        else:
            self.__word_count.Print("词表路径错误")
            return
        # 读取原文路径
        src_text_path = self.__setting.GetSettingWidget().srcFilePathEdit.text().replace("\n", "")
        self.__word_count.Print("开始读取原文文件...")
        print(src_text_path)
        if len(src_text_path) > 4 and src_text_path[len(src_text_path) - 4:len(src_text_path)] == ".txt":
            self.__word_count.Print("成功读取原文文件")
        else:
            self.__word_count.Print("原文文件路径错误")
            return
        self.__word_count.Print("开始统计，耗时很久，请不要关闭")
        bishop_counter.ParseSrcFile(src_text_path)
        word_map = bishop_counter.GetWordCount()
        for word in word_map:
            self.__word_count.Print(word[0]+" "+str(word[1]))
