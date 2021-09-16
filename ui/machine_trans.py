import sys
from PyQt5.Qt import *
from PyQt5 import QtGui
from ui.ui_machine_trans import Ui_MachineTrans


class MachineTrans(QWidget):
    __ui_machine_trans = 0

    def Init(self):
        self.__ui_machine_trans = Ui_MachineTrans()
        self.__ui_machine_trans.setupUi(self)
        # 打开原文文件信号与槽
        self.__ui_machine_trans.openSrcFileButton.clicked.connect(self.__OpenFileDialog)

    def __OpenFileDialog(self):
        res = QFileDialog.getOpenFileName(self, "打开原文文件", "./", "Text Files (*.txt)")
        src_file_path = res[0]
        if src_file_path != "":
            self.__ui_machine_trans.srcFilePathEdit.setText(src_file_path)

    def Print(self, text):
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.__ui_machine_trans.textBrowser.setFont(font)
        self.__ui_machine_trans.textBrowser.append(text)

    def GetMachineTransWidget(self):
        return self.__ui_machine_trans

    def Show(self):
        self.__ui_machine_trans.machineTransWidget.show()

    def Hide(self):
        self.__ui_machine_trans.machineTransWidget.hide()
