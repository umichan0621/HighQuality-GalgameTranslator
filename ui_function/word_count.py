import sys
from PyQt5.Qt import *
from PyQt5 import QtGui
from ui.ui_word_count import Ui_WordCount


class WordCount(QWidget):
    ui_word_count = 0
    __font = 0

    def Init(self):
        self.ui_word_count = Ui_WordCount()
        self.ui_word_count.setupUi(self)
        # 设置字体
        self.__font = QtGui.QFont()
        self.__font.setFamily("宋体")
        self.__font.setPointSize(16)
        self.Hide()

    def Print(self, text):
        self.ui_word_count.wordCountBrowser.setFont(self.__font)
        self.ui_word_count.wordCountBrowser.append(text)
        self.ui_word_count.wordCountBrowser.repaint()

    def GetWordCountWidget(self):
        return self.ui_word_count

    def Show(self):
        self.ui_word_count.wordCountWidget.show()

    def Hide(self):
        self.ui_word_count.wordCountWidget.hide()
