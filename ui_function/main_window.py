import sys
import time
from PyQt5.Qt import QApplication, QWidget
from ui_function.menu import Menu
from ui_function.setting import Setting
from ui_function.machine_translator import MachineTrans
from ui_function.word_counter import WordCount
from plugins.bishop_translator import BishopTranslator
from plugins.bishop_counter import BishopCounter


class MainWindow:

    def __init__(self):
        super().__init__()
        app = QApplication(sys.argv)
        self.__bishop_counter = BishopCounter()
        self.__bishop_translator = BishopTranslator()
        self.__main_window = QWidget()
        self.__static = -1
        self.__menu = Menu(self.__main_window)  # 初始化菜单栏
        self.__machine_trans = MachineTrans(self.__main_window)  # 初始化机器翻译窗体
        self.__word_count = WordCount(self.__main_window)  # 初始化统计窗体
        self.__setting = Setting(self.__main_window)  # 初始化设置窗体
        # 设置Menu窗体按钮的信号和槽
        self.__menu.GetMenuWidget().settingButton.clicked.connect(self.__ChangeToSetting)
        self.__menu.GetMenuWidget().machineTranslateButton.clicked.connect(self.__ChangeToMachineTrans)
        self.__menu.GetMenuWidget().wordCountButton.clicked.connect(self.__ChangeToWordCount)
        # 设置机器翻译开始翻译按钮的信号和槽
        self.__machine_trans.GetStartTransButton().clicked.connect(self.CallPluginBishopTrans)
        # 设置词频统计开始统计按钮的信号和槽
        self.__word_count.GetStartCountButton().clicked.connect(self.CallPluginBishopCount)
        # 0表示MachineTrans窗体，1表示WordCount窗体，2表示Setting窗体
        self.__ChangeToMachineTrans()
        self.__main_window.setWindowTitle("HighQuality-GalgameTranslator")
        self.__main_window.setFixedSize(960, 720)
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

    def CallPluginBishopTrans(self):
        # 读取词表路径
        word_dic_path = self.__setting.GetWordsDicEdit()
        # 读取原文路径
        src_text_path = self.__setting.GetSrcFilePathEdit()
        # 读取翻译API的ID和Key
        api_id = self.__setting.GetTencentApiId()
        api_key = self.__setting.GetTencentApiKey()
        self.__bishop_translator.Init(word_dic_path, src_text_path, api_id, api_key)
        self.__bishop_translator.print_signal.connect(self.__machine_trans.Print)
        self.__bishop_translator.start()

    def CallPluginBishopCount(self):
        # 读取词表路径
        word_dic_path = self.__setting.GetWordsDicEdit()
        # 读取原文路径
        src_text_path = self.__setting.GetSrcFilePathEdit()
        self.__bishop_counter.print_signal.connect(self.__word_count.Print)
        self.__bishop_counter.Init(word_dic_path, src_text_path)
        self.__bishop_counter.start()
