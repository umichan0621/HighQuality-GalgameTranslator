import sys
from PyQt5.Qt import *
from ui.ui_setting import Ui_Setting


class Setting(QWidget):
    __ui_setting = 0

    def Init(self):
        self.__ui_setting = Ui_Setting()
        self.__ui_setting.setupUi(self)
        self.__ui_setting.openWordsDicButton.clicked.connect(self.__OpenFileDialog)
        self.__ui_setting.configSaveButton.clicked.connect(self.__ConfigSave)
        self.LoadAPIIDAndKey()
        self.Hide()

    def GetSettingWidget(self):
        return self.__ui_setting

    def Show(self):
        self.__ui_setting.settingWidget.show()

    def Hide(self):
        self.__ui_setting.settingWidget.hide()

    def LoadAPIIDAndKey(self):
        config_file = open("../config.ini", 'a+', encoding="utf-8")
        config_file.write("")
        config_file = open("../config.ini", 'r', encoding="utf-8")
        # 读取config文件并写入
        content = config_file.readlines()
        if len(content) >= 3:
            self.__ui_setting.wordsDicEdit.setText(content[0])
            self.__ui_setting.txAPIIDEdit.setText(content[1])
            self.__ui_setting.txAPIKeyEdit.setText(content[2])

        self.__ui_setting.txAPIIDEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.__ui_setting.txAPIKeyEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    def __ConfigSave(self):
        config_file = open("../config.ini", 'w', encoding="utf-8")
        config_file.write(self.__ui_setting.wordsDicEdit.text()+"\n")
        config_file.write(self.__ui_setting.txAPIIDEdit.text()+"\n")
        config_file.write(self.__ui_setting.txAPIKeyEdit.text()+"\n")

    def __OpenFileDialog(self):
        res = QFileDialog.getOpenFileName(self, "打开词表", "./", "Excel Files (*.xlsx)")
        src_file_path = res[0]
        if src_file_path != "":
            self.__ui_setting.wordsDicEdit.setText(src_file_path)