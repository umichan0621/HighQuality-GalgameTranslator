import sys
import time
from PyQt5.Qt import *
from ui.menu import Menu
from ui.setting import Setting
from ui.machine_trans import MachineTrans
from plugins.bishop import BishopTranslator


class MainWindow:
    # 0表示MachineTrans窗体，1表示，2表示Setting窗体
    __static = 0
    __main_window = 0
    __menu = 0
    __setting = 0
    __machine_trans = 0

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
        # 初始化设置窗体
        self.__setting = Setting()
        self.__setting.Init()
        self.__setting.GetSettingWidget().settingWidget.setParent(self.__main_window)
        # 设置Menu窗体按钮的信号和槽
        self.__menu.GetMenuWidget().settingButton.clicked.connect(self.ChangeToSetting)
        self.__menu.GetMenuWidget().machineTranslateButton.clicked.connect(self.ChangeToMachineTrans)
        # 设置机器翻译开始翻译按钮的信号和槽
        self.__machine_trans.GetMachineTransWidget().startTransButton.clicked.connect(self.PluginBishop)
        # 启动主窗体
        self.__main_window.show()
        sys.exit(app.exec_())

    def ChangeToSetting(self):
        if self.__static == 0:
            self.__machine_trans.Hide()
            self.__setting.Show()
        self.__static = 2

    def ChangeToMachineTrans(self):
        if self.__static == 2:
            self.__setting.Hide()
            self.__machine_trans.Show()
        self.__static = 0

    def PluginBishop(self):
        bishop_translator = BishopTranslator()
        src_text_path = self.__machine_trans.GetMachineTransWidget().srcFilePathEdit.text()
        if len(src_text_path) > 4 and src_text_path[len(src_text_path) - 4:len(src_text_path)] == ".txt":
            bishop_translator.SetSourceTextPath(src_text_path)
        word_dic_path = self.__setting.GetSettingWidget().wordsDicEdit.text().replace("\n", "")
        print(word_dic_path[len(word_dic_path) - 5:5])
        if len(word_dic_path) > 5 and word_dic_path[len(word_dic_path) - 5:len(word_dic_path)] == ".xlsx":
            bishop_translator.SetWordDicPath(word_dic_path)
        api_id = self.__setting.GetSettingWidget().txAPIIDEdit.text().replace("\n", "")
        api_key = self.__setting.GetSettingWidget().txAPIKeyEdit.text().replace("\n", "")
        bishop_translator.SetGeneralTrans(api_id, api_key)
        while bishop_translator.GetCurLine() < bishop_translator.GetTotalLine():
            res = bishop_translator.HandleText()
            if len(res) == 2:
                self.__machine_trans.Print(res[0].replace("\n", ""))
                self.__machine_trans.Print(res[1])
                self.__machine_trans.Print("")
            else:
                self.__machine_trans.Print("Address:"+res[0][11:18])
            time.sleep(0.1)
