from PyQt5.Qt import QWidget
from PyQt5 import QtGui
from ui.ui_word_counter import Ui_WordCount


class WordCount(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui_word_count = Ui_WordCount()
        self.ui_word_count.setupUi(self)
        self.ui_word_count.wordCountWidget.setParent(parent)
        # 设置字体
        self.__font = QtGui.QFont()
        self.__font.setFamily("宋体")
        self.__font.setPointSize(16)
        self.Hide()

    def GetStartCountButton(self):
        return self.ui_word_count.startCountButton

    def Print(self, text):
        self.ui_word_count.wordCountBrowser.setFont(self.__font)
        self.ui_word_count.wordCountBrowser.append(text)
        self.ui_word_count.wordCountBrowser.repaint()

    def Show(self):
        self.ui_word_count.wordCountWidget.show()

    def Hide(self):
        self.ui_word_count.wordCountWidget.hide()
