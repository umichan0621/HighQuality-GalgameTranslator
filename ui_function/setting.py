from PyQt5.Qt import QWidget, QFileDialog, QLineEdit, QDesktopServices, QUrl
from PyQt5 import QtGui
from ui.ui_setting import Ui_Setting
from machine_translator.general_translator import TranslatorApi


class Setting(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.__ui_setting = Ui_Setting()
        self.__ui_setting.setupUi(self)
        self.__ui_setting.settingWidget.setParent(parent)
        self.__ui_setting.openWordsDicButton.clicked.connect(self.__OpenDicFileDialog)
        self.__ui_setting.openSrcFileButton.clicked.connect(self.__OpenSrcFileDialog)
        online_excel_url = 'https://docs.google.com/spreadsheets/' \
                           'd/1anIXXcQiWM1ke6veDIBHw4kmheULIdy7tGXPLjScIcU/' \
                           'edit#gid=1495071713'
        self.__ui_setting.openOnlineDicButton.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(online_excel_url)))
        self.__ui_setting.configSaveButton.clicked.connect(self.__ConfigSave)
        # 设置字体
        self.__font = QtGui.QFont()
        self.__font.setFamily("宋体")
        self.__ui_setting.testTranslateEdit.setFont(self.__font)
        self.__ui_setting.selectTranslatorComboBox.addItem("google翻译")
        self.__ui_setting.selectTranslatorComboBox.addItem("腾讯翻译")
        self.__select_translate_map = {"google翻译": TranslatorApi.GOOGLE_TRANS,
                                       "腾讯翻译": TranslatorApi.TENCENT_TRANS}
        self.__LoadAPIIDAndKey()
        self.Hide()

    def GetWordsDicEdit(self):
        return self.__ui_setting.wordsDicEdit.text().replace("\n", "")

    def GetSrcFilePathEdit(self):
        return self.__ui_setting.srcFilePathEdit.text().replace("\n", "")

    def GetTencentApiId(self):
        return self.__ui_setting.tencentApiIdEdit.text().replace("\n", "")

    def GetTencentApiKey(self):
        return self.__ui_setting.tencentApiKeyEdit.text().replace("\n", "")

    def GetTestText(self):
        return self.__ui_setting.testTranslateEdit.toPlainText().replace("\n", "")

    def GetTestTranslateButton(self):
        return self.__ui_setting.testTranslateButton

    def GetSelectedTranslateApi(self):
        select_api = self.__ui_setting.selectTranslatorComboBox.currentText()
        return self.__select_translate_map[select_api]

    def Print(self, text):
        self.__ui_setting.testTranslateBrowser.setFont(self.__font)
        self.__ui_setting.testTranslateBrowser.clear()
        self.__ui_setting.testTranslateBrowser.append(text)
        self.__ui_setting.testTranslateBrowser.repaint()

    def Show(self):
        self.__ui_setting.settingWidget.show()

    def Hide(self):
        self.__ui_setting.settingWidget.hide()

    def __LoadAPIIDAndKey(self):
        config_file = open("config.ini", 'a+', encoding="utf-8")
        config_file.write("")
        config_file = open("config.ini", 'r', encoding="utf-8")
        # 读取config文件并写入
        content = config_file.readlines()
        if len(content) >= 4:
            self.__ui_setting.wordsDicEdit.setText(content[0])
            self.__ui_setting.srcFilePathEdit.setText(content[1])
            self.__ui_setting.tencentApiIdEdit.setText(content[2])
            self.__ui_setting.tencentApiKeyEdit.setText(content[3])
        self.__ui_setting.tencentApiIdEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.__ui_setting.tencentApiKeyEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    def __ConfigSave(self):
        config_file = open("config.ini", 'w', encoding="utf-8")
        config_file.write(self.__ui_setting.wordsDicEdit.text().replace('\n', '') + '\n')
        config_file.write(self.__ui_setting.srcFilePathEdit.text().replace('\n', '') + '\n')
        config_file.write(self.__ui_setting.tencentApiIdEdit.text().replace('\n', '') + '\n')
        config_file.write(self.__ui_setting.tencentApiKeyEdit.text().replace('\n', '') + '\n')

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
