from machine_translator.tencent_translator import TencentMachineTranslator
from machine_translator.google_translator import GoogleMachineTranslator


class GeneralTranslator:
    def __init__(self, tencent_api_id='', tencent_api_key=''):
        self.__tencent_translator = TencentMachineTranslator(tencent_api_id, tencent_api_key)
        self.__google_translator = GoogleMachineTranslator()

    def Translate(self, source_text):
        return self.__tencent_translator.Translate(source_text)

