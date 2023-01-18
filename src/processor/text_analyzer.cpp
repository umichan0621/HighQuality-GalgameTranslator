#include "text_analyzer.h"

#include <utils/string.hpp>

namespace gal {
namespace processor {

TextAnalyzer::TextAnalyzer() : newline_character_("\\n") { separator_.insert({newline_character_, ""}); }

void TextAnalyzer::SetNewlineCharacter(const std::string& newline_character) {
    separator_.erase(newline_character_);
    newline_character_ = newline_character;
    separator_.insert({newline_character_, ""});
}

void TextAnalyzer::AddUnnecessaryNewlineCharacter(const std::string& unnecessary_newline_character) {
    unnecessary_newline_character_.insert(unnecessary_newline_character);
}

void TextAnalyzer::AddRegex(const std::string& regex_str) { regex_vec_.insert(regex_str); }

void TextAnalyzer::AddSeparator(const std::string& separator, const std::string& translation) {
    separator_[separator] = translation;
}

std::vector<AnalyzerRes> TextAnalyzer::Analyze(const std::string& text) {
    std::vector<AnalyzerRes> res;
    std::string tmp_text = text;
    // delete unnecessary newline character
    for (const auto& str : unnecessary_newline_character_) {
        std::string target = str;
        utils::Replace(&target, newline_character_, "");
        utils::Replace(&tmp_text, str, target);
    }
    // full text match
    for (const auto& regex : regex_vec_) {
        if (std::regex_match(tmp_text, std::regex(regex))) {
            res.push_back({false, tmp_text});
            return res;
        }
    }
    // split the text
    res.push_back({true, tmp_text});

    for (const auto& separator : separator_) {
        std::vector<AnalyzerRes> temp;
        for (auto& analyzer_res : res) {
            // no need for tranlation
            if (!analyzer_res.need_tranlate || !NeedTranslate(&analyzer_res.text)) {
                if (temp.size() > 0 && false == temp.back().need_tranlate) {
                    temp.back().text += analyzer_res.text;
                } else {
                    temp.emplace_back(analyzer_res);
                }
                continue;
            }
            std::vector<std::string> split_res = utils::Split(analyzer_res.text, separator.first, true);
            for (std::string split_text : split_res) {
                if (split_text.empty()) {
                    continue;
                }
                // Analyzer the sub text
                if (!NeedTranslate(&split_text)) {
                    // Merge the text that no need to translate
                    if (temp.size() > 0 && false == temp.back().need_tranlate) {
                        temp.back().text += split_text;
                    } else {
                        temp.push_back({false, split_text});
                    }
                } else {
                    temp.push_back({true, split_text});
                }
            }
        }
        res.swap(temp);
    }
    return res;
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
