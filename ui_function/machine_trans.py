import sys
from PyQt5.Qt import *
from PyQt5 import QtGui
from ui.ui_machine_trans import Ui_MachineTrans


class MachineTrans(QWidget):
    __ui_machine_trans = 0
    __font = 0

    def Init(self):
        self.__ui_machine_trans = Ui_MachineTrans()
        self.__ui_machine_trans.setupUi(self)
        # 设置字体
        self.__font = QtGui.QFont()
        self.__font.setFamily("宋体")
        self.__font.setPointSize(16)
        self.Hide()

    def Print(self, text):
        self.__ui_machine_trans.machineTransBrowser.setFont(self.__font)
        self.__ui_machine_trans.machineTransBrowser.append(text)
        self.__ui_machine_trans.machineTransBrowser.repaint()

    def GetMachineTransWidget(self):
        return self.__ui_machine_trans

    def Show(self):
        self.__ui_machine_trans.machineTransWidget.show()

    def Hide(self):
        self.__ui_machine_trans.machineTransWidget.hide()
