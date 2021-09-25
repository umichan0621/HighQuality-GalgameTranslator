from PyQt5.Qt import QWidget
from PyQt5 import QtGui
from ui.ui_machine_translator import Ui_MachineTrans


class MachineTrans(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.__ui_machine_trans = Ui_MachineTrans()
        self.__ui_machine_trans.setupUi(self)
        self.__ui_machine_trans.machineTransWidget.setParent(parent)
        # 设置字体
        self.__font = QtGui.QFont()
        self.__font.setFamily("宋体")
        self.__font.setPointSize(16)
        self.Hide()

    def GetStartTransButton(self):
        return self.__ui_machine_trans.startTransButton

    def Print(self, text):
        self.__ui_machine_trans.machineTransBrowser.setFont(self.__font)
        self.__ui_machine_trans.machineTransBrowser.append(text)
        self.__ui_machine_trans.machineTransBrowser.repaint()

    def Show(self):
        self.__ui_machine_trans.machineTransWidget.show()

    def Hide(self):
        self.__ui_machine_trans.machineTransWidget.hide()
