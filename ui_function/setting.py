from PyQt5.Qt import QWidget
from PyQt5.Qt import QFileDialog
from ui.ui_setting import Ui_Setting
from PyQt5.Qt import QLineEdit
from PyQt5.Qt import QDesktopServices
from PyQt5.Qt import QUrl


class Setting(QWidget):
    __ui_setting = 0

    def Init(self):
        self.__ui_setting = Ui_Setting()
        self.__ui_setting.setupUi(self)
        self.__ui_setting.openWordsDicButton.clicked.connect(self.__OpenDicFileDialog)
        self.__ui_setting.openSrcFileButton.clicked.connect(self.__OpenSrcFileDialog)
        online_excel_url = "https://docs.google.com/spreadsheets/d/1anIXXcQiWM1ke6veDIBHw4kmheULIdy7tGXPLjScIcU/edit#gid=1495071713"
        self.__ui_setting.openOnlineDicButton.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(online_excel_url)))
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
        config_file = open("config.ini", 'a+', encoding="utf-8")
        config_file.write("")
        config_file = open("config.ini", 'r', encoding="utf-8")
        # 读取config文件并写入
        content = config_file.readlines()
        if len(content) >= 4:
            self.__ui_setting.wordsDicEdit.setText(content[0])
            self.__ui_setting.srcFilePathEdit.setText(content[1])
            self.__ui_setting.txAPIIDEdit.setText(content[2])
            self.__ui_setting.txAPIKeyEdit.setText(content[3])

        self.__ui_setting.txAPIIDEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.__ui_setting.txAPIKeyEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    def __ConfigSave(self):
        config_file = open("config.ini", 'w', encoding="utf-8")
        config_file.write(self.__ui_setting.wordsDicEdit.text().replace('\n', '') + '\n')
        config_file.write(self.__ui_setting.srcFilePathEdit.text().replace('\n', '') + '\n')
        config_file.write(self.__ui_setting.txAPIIDEdit.text().replace('\n', '') + '\n')
        config_file.write(self.__ui_setting.txAPIKeyEdit.text().replace('\n', '') + '\n')

    def __OpenDicFileDialog(self):
        res = QFileDialog.getOpenFileName(self, "打开词表", "./", "Excel Files (*.xlsx)")
        src_file_path = res[0]
        if src_file_path != "":
            self.__ui_setting.wordsDicEdit.setText(src_file_path)

    def __OpenSrcFileDialog(self):
        res = QFileDialog.getOpenFileName(self, "打开原文文件", "./", "Text Files (*.txt)")
        src_file_path = res[0]
        if src_file_path != "":
            self.__ui_setting.srcFilePathEdit.setText(src_file_path)
