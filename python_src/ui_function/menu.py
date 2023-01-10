from PyQt5.Qt import QWidget
from ui.ui_menu import Ui_Menu


class Menu(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.__ui_menu = Ui_Menu()
        self.__ui_menu.setupUi(self)
        self.__ui_menu.menuWidget.setParent(parent)

    def GetMenuWidget(self):
        return self.__ui_menu

    def Show(self):
        self.__ui_menu.menuWidget.show()

    def Hide(self):
        self.__ui_menu.menuWidget.hide()
