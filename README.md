# HighQuality-GalgameTranslator

## About HighQuality-GalgameTranslator
- 基于Python，用于翻译Galgame提取的特定格式日语文本的机器翻译程序
- 通过建立字典，直接翻译字典内文本，解决机器翻译在翻译部分词语或句子时效果很差的问题
- 机器翻译在处理拟声词或和谐词时效果极差
- 如果字典很完善，那么翻译的效果将会十分优秀
- 基于词频统计，可以收录文本内的通用高频词
- 基于词频统计，也可以收录文本内的特殊词

## 依赖库
1. TX机器翻译API
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
4. PyQt5
```
pip install PyQt5
pip install PyQt5-tools
```
## 提取游戏内文本
- Tiny翻译肋手用于提取游戏文本，目前支持的会社有Bishop、WillPlus、YU-RIS、Kaguya、RealLive、PJADV、AliceSoft
- [Tiny翻译肋手(提取码:fo2c)](https://pan.baidu.com/s/1aDaKYD96wW0z9ezfvdUfOA#list/path=%2F)

- winhex用于查询游戏文本在文件内的偏移量
- [winhex(提取码:eq2w)](https://pan.baidu.com/s/10XaxPtgCZhY5eRxca2t7FQ)


## 如何协助完成高质量的Galgame机器翻译
- 协助开发Python翻译脚本
- 使用内置的词频统计工具count_word_frequency.py统计未收录的通用高频词
    - 只会将第二列不为空，即有中文翻译的词加入字典
    - 对于机器翻译完全正确的词语请放在excel的[过滤]页下
- 统计某部作品的专有词
    - 对于某部作品的专有词请放在excel的[特殊]页下
- 协助完成字典内收录词语的翻译

## 协助完善词表
- 请确保可以使用Google
- [Google在线文档](https://docs.google.com/spreadsheets/d/1anIXXcQiWM1ke6veDIBHw4kmheULIdy7tGXPLjScIcU/edit#gid=1495071713)
- 需要协助开发可以申请修改权限，但不要随意胡乱修改文档
- [在线聊天室](https://gitter.im/HighQuality-GalgameTranslator/community)，开发和使用相关问题讨论
