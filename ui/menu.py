from ui.ui_menu import Ui_Menu
from PyQt5.Qt import QWidget


class Menu(QWidget):
    __ui_menu = 0

    def Init(self):
        self.__ui_menu = Ui_Menu()
        self.__ui_menu.setupUi(self)

    def GetMenuWidget(self):
        return self.__ui_menu

    def Show(self):
        self.__ui_menu.menuWidget.show()

    def Hide(self):
        self.__ui_menu.menuWidget.hide()
