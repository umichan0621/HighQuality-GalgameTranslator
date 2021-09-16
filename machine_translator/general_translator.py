from machine_translator.tencent_translator import TencentMachineTranslator


class GeneralTranslator:
    __machine_translator = TencentMachineTranslator()

    def SetApiIdAndKey(self, api_id, api_key):
        self.__machine_translator.SetIdAndKey(api_id, api_key)

    def Translate(self, source_text):
        return self.__machine_translator.Translate(source_text)

