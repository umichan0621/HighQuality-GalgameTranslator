#include "text_analyzer.h"

#include <utils/string.hpp>

namespace gal {
namespace processor {

TextAnalyzer::TextAnalyzer() : newline_character_("\\n") {}

void TextAnalyzer::SetNewlineCharacter(const std::string& newline_character) { newline_character_ = newline_character; }

void TextAnalyzer::AddNewlineCharacterTrigger(const std::string& newline_character_trigger) {
    newline_character_trigger_.insert(newline_character_trigger);
}

void TextAnalyzer::AddRegex(const std::string& regex_str) { regex_vec_.insert(regex_str); }

void TextAnalyzer::AddSeparator(const std::string& separator, const std::string& translation) {
    separator_[separator] = translation;
}

std::vector<utils::AnalyzerRes> TextAnalyzer::Analyze(std::string text) {
    utils::Replace(&text, "、" + newline_character_, "、");
    std::vector<utils::AnalyzerRes> analyzer_res;
    // full text match
    for (const auto& regex : regex_vec_) {
        if (std::regex_match(text, std::regex(regex))) {
            analyzer_res.push_back({false, text});
            return analyzer_res;
        }
    }
    // split text by newline character
    std::vector<std::string> split_res = utils::Split(text, newline_character_, true);
    for (int i = 0; i < split_res.size() - 1; ++i) {
        SplitTextByNewlineCharacter(&analyzer_res, split_res[i], split_res[i + 1]);
    }
    SplitTextByNewlineCharacter(&analyzer_res, split_res[split_res.size() - 1], "");
    // split text recursively
    for (const auto& separator : separator_) {
        SplitText(&analyzer_res, separator.first, separator.second);
    }
    return analyzer_res;
}

void TextAnalyzer::SplitTextByNewlineCharacter(
    std::vector<utils::AnalyzerRes>* analyzer_res, const std::string& sub_text, const std::string& next_text) {
    // text
    if (sub_text != newline_character_) {
        // merge two text that need to be translated
        if (analyzer_res->size() > 0 && analyzer_res->back().need_tranlate) {
            analyzer_res->back().text += sub_text;
        } else {
            analyzer_res->push_back({true, sub_text});
        }
        return;
    }
    // newline character
    if (analyzer_res->empty()) {
        analyzer_res->push_back({false, sub_text});
        return;
    }
    auto& pre_res = analyzer_res->back();
    for (const auto& regex : newline_character_trigger_) {
        if (std::regex_match(pre_res.text, std::regex(regex))) {
            analyzer_res->push_back({false, sub_text});
            return;
        }
    }
    // processor separator
    for (const auto& separator : separator_) {
        int pos_pre = pre_res.text.find(separator.first);
        int pos_next = next_text.find(separator.first);
        if (pos_pre < 0 && pos_next < 0) {
            continue;
        }
        // separator at begin of next text / end of pre text
        if (pos_next == 0 || pos_pre >= 0 && pos_pre + separator.first.size() == pre_res.text.size()) {
            analyzer_res->push_back({false, sub_text});
            return;
        }
    }
}

void TextAnalyzer::SplitText(
    std::vector<utils::AnalyzerRes>* analyzer_res, const std::string& separator, const std::string& translation) {
    std::vector<utils::AnalyzerRes> temp;
    for (auto& sub_res : *analyzer_res) {
        // no need for tranlation
        if (!sub_res.need_tranlate || !NeedTranslate(&sub_res.text)) {
            if (temp.size() > 0 && false == temp.back().need_tranlate) {
                temp.back().text += sub_res.text;
            } else {
                temp.emplace_back(sub_res);
            }
            continue;
        }
        std::vector<std::string> split_res = utils::Split(sub_res.text, separator, true);
        for (std::string split_text : split_res) {
            if (split_text.empty()) {
                continue;
            }
            // Analyzer the sub text
            if (!NeedTranslate(&split_text)) {
                // Merge the text that no need to translate
                if (temp.size() > 0 && !temp.back().need_tranlate) {
                    temp.back().text += split_text;
                } else {
                    temp.push_back({false, split_text});
                }
            } else {
                temp.push_back({true, split_text});
            }
        }
    }
    analyzer_res->swap(temp);
}

bool TextAnalyzer::NeedTranslate(std::string* text) {
    // full text match
    for (const auto& regex : regex_vec_) {
        if (std::regex_match(*text, std::regex(regex))) {
            return false;
        }
    }
    for (const auto& separator : separator_) {
        if (*text == separator.first) {
            if (separator.second != "") {
                *text = separator.second;
            }
            return false;
        }
    }
    return true;
}

}  // namespace processor
}  // namespace gal
