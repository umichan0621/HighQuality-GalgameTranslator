from PyQt5.Qt import QThread, pyqtSignal
from machine_translator.general_translator import GeneralTranslator
from machine_translator.general_translator import TranslatorApi


class TestTranslator(QThread):
    print_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__general_translator = GeneralTranslator()
        self.__source_text = ""
        self.__translate_api = None

    def SetTencentTranslator(self, tencent_api_id='', tencent_api_key=''):
        self.__general_translator.SetTencentTranslator(tencent_api_id, tencent_api_key)

    def SetTranslateContent(self, source_text, translate_api=TranslatorApi.GOOGLE_TRANS):
        self.__source_text = source_text
        self.__translate_api = translate_api

    def run(self):
        res = self.__general_translator.Translate(self.__source_text, self.__translate_api)
        self.print_signal.emit(res)
