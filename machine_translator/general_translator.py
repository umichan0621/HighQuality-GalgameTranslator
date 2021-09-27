from enum import Enum
from machine_translator.tencent_translator import TencentMachineTranslator
from machine_translator.google_translator import GoogleMachineTranslator


class TranslatorApi(Enum):
    NULL_TRANS = -1
    GOOGLE_TRANS = 0
    TENCENT_TRANS = 1


class GeneralTranslator:
    def __init__(self):
        self.__tencent_translator = None
        self.__google_translator = GoogleMachineTranslator()
        self.__translator_map = {TranslatorApi.GOOGLE_TRANS: self.__google_translator}

    def SetTencentTranslator(self, tencent_api_id='', tencent_api_key=''):
        self.__tencent_translator = TencentMachineTranslator(tencent_api_id, tencent_api_key)
        self.__translator_map[TranslatorApi.TENCENT_TRANS] = self.__tencent_translator

    def Translate(self, source_text, translate_api=TranslatorApi.GOOGLE_TRANS):
        if translate_api == TranslatorApi.NULL_TRANS:
            return 'NULL'
        return self.__translator_map[translate_api].Translate(source_text)
