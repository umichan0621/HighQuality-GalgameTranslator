from function.machine_translator import TextTranslator

api_id = "api_id"
api_key = "api_key"
text_translator = TextTranslator()
text_translator.SetExcelPath("dictionary.xlsx")
text_translator.SetIdAndKey(api_id, api_key)
text_translator.SetOutputPath("output.txt")
text_translator.Parse("example.txt", "utf-16le")
