# HighQuality-GalgameTranslator

## About HighQuality-GalgameTranslator
- 基于Python，用于翻译Galgame提取的特定格式日语文本的机器翻译程序
- 通过建立字典，直接翻译字典内文本，解决机器翻译在翻译部分词语或句子时效果很差的问题
- 机器翻译在处理拟声词或和谐词时效果极差
- 如果字典很完善，那么翻译的效果将会十分优秀
- 基于词频统计，可以收录文本内的通用高频词
- 基于词频统计，也可以收录文本内的特殊词

## 如何使用？
- 利用Tiny翻译肋手和winhex（下面有链接）从游戏文件中提取游戏文本
- 在【设置】中填写翻译API、游戏文本路径和词表（右侧有google在线文档链接下载）
- 在【机器翻译】点击【开始翻译】，会自动逐行翻译
- 利用Tiny翻译肋手将翻译之后的文本导入游戏文件

## 具体功能
- 已完成
  - 针对Bishop游戏的机器翻译√
  - 针对Bishop游戏的词频统计√
  - 腾讯翻译API√
  - Google翻译API√
- 待完成
  - 针对Kaguya游戏的机器翻译
  - 针对Kaguya游戏的词频统计
  - 人工翻译校对工具

## 依赖库
- Shift + 右键 点击项目文件夹空白处
- 在此处打开命令窗口(打开Powershell窗口) 
- 在其中运行
```
py -m pip install -r requirements.txt
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
    - 对于机器翻译完全正确的词语请放在excel的[过滤词表]页下
- 统计某部作品的专有词
    - 对于某部作品的专有词请放在excel的[特殊词表]页下
- 协助完成字典内收录词语的翻译

## 协助完善词表
- 请确保可以使用Google
- [Google在线文档](https://docs.google.com/spreadsheets/d/1anIXXcQiWM1ke6veDIBHw4kmheULIdy7tGXPLjScIcU/edit#gid=1495071713)
- 需要协助开发可以申请修改权限
- 仅下载不对词表进行修改不要申请权限
- [在线聊天室](https://gitter.im/HighQuality-GalgameTranslator/community)，开发和使用相关问题讨论
