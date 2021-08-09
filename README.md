# HighQuality-GalgameTranslator

## About HighQuality-GalgameTranslator
    - 基于Python，用于翻译特定格式日语文本的机器翻译程序
    - 通过建立字典，直接翻译字典内文本，解决机器翻译在翻译部分词语或句子时效果很差的问题
    - 如果字典很完善，那么翻译的效果将会十分优秀
    - 基于词频统计，可以收录文本内的高频词

## 依赖库
1. TX翻译
```
pip install --upgrade tencentcloud-sdk-python
```
2. excel读取
```
pip install xlrd
```
3. 日语分词
```
pip install mecab-python3
```