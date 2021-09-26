from pygoogletranslation import Translator


class GoogleMachineTranslator:
    def __init__(self):
        self.__translator = Translator(service_url='translate.google.cn')

    def Translate(self, source_text):
        try:
            translate_res = self.__translator.translate(source_text, src='ja', dest='zh-CN')
            return translate_res.text
        except Exception:
            return "ERROR"
