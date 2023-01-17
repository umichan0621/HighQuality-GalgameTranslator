#include "text_processor.h"

#include <algorithm>

#include <utils/string.hpp>

namespace gal {
namespace processor {

static std::string generate_random_str() {
    std::string res = "";
    res += 'A' + rand() % 26;
    res += '-';
    res += '0' + rand() % 10;
    res += '0' + rand() % 10;
    return res;
}

TextProcessor::TextProcessor() : need_sort_(true) {}

std::string TextProcessor::Process(const std::string& text) {
    std::string res = text;
    for (const std::string& word : word_list()) {
        if (word_tmp_dic_.count(word) != 0) {
            const std::string tmp = word_tmp_dic_[word];
            utils::Replace(&res, word, tmp);
        }
    }
    return res;
}

std::string TextProcessor::Recover(const std::string& text) {
    std::string res = text;
    for (auto& pair : tmp_trans_dic_) {
        const std::string& tmp = pair.first;
        const std::string& trans = pair.second;
        utils::Replace(&res, tmp, trans);
    }
    return res;
}

void TextProcessor::InsertWord(const std::string& word, const std::string& translation) {
    std::string tmp;
    // same translation exists
    if (trans_tmp_dic_.count(translation) != 0) {
        tmp = trans_tmp_dic_[translation];
    } else {
        tmp = generate_random_str();
        while (tmp_trans_dic_.count(tmp) != 0) {
            tmp = generate_random_str();
        }
        tmp_trans_dic_[tmp] = translation;
        trans_tmp_dic_[translation] = tmp;
    }
    word_tmp_dic_[word] = tmp;
    word_list_.emplace_back(word);
    need_sort_ = true;
}

void TextProcessor::InsertWord(const std::string& word, const std::string& translation, str_func random_str) {
    std::string tmp;
    // same translation exists
    if (trans_tmp_dic_.count(translation) != 0) {
        tmp = trans_tmp_dic_[translation];
    } else {
        tmp = random_str();
        while (tmp_trans_dic_.count(tmp) != 0) {
            tmp = random_str();
        }
        tmp_trans_dic_[tmp] = translation;
        trans_tmp_dic_[translation] = tmp;
    }
    word_tmp_dic_[word] = tmp;
    word_list_.emplace_back(word);
    need_sort_ = true;
}

void TextProcessor::InsertName(GalName gal_name) {
    const auto& first_name = gal_name.first_name;
    const auto& first_name_translation = gal_name.first_name_translation;
    const auto& last_name = gal_name.last_name;
    const auto& last_name_translation = gal_name.last_name_translation;
    InsertWord(first_name, first_name_translation);
    InsertWord(last_name, last_name_translation);
    for (auto& process : gal_name.process_vec) {
        // Process name and get the word
        std::string word, translation;
        if (process.is_first_name) {
            word = first_name;
            translation = first_name_translation;
        } else {
            word = last_name;
            translation = last_name_translation;
        }
        if (process.is_tail) {
            word = word + process.word;
        } else {
            word = process.word + word;
        }
        if (process.is_translation_tail) {
            translation = translation + process.translation;
        } else {
            translation = process.translation + translation;
        }
        InsertWord(word, translation);
    }
}

void TextProcessor::InsertName(GalName gal_name, str_func random_str) {
    const auto& first_name = gal_name.first_name;
    const auto& first_name_translation = gal_name.first_name_translation;
    const auto& last_name = gal_name.last_name;
    const auto& last_name_translation = gal_name.last_name_translation;
    InsertWord(first_name, first_name_translation, random_str);
    InsertWord(last_name, last_name_translation, random_str);
    for (auto& process : gal_name.process_vec) {
        // Process name and get the word
        std::string word, translation;
        if (process.is_first_name) {
            word = first_name;
            translation = first_name_translation;
        } else {
            word = last_name;
            translation = last_name_translation;
        }
        if (process.is_tail) {
            word = word + process.word;
        } else {
            word = process.word + word;
        }
        if (process.is_translation_tail) {
            translation = translation + process.translation;
        } else {
            translation = process.translation + translation;
        }
        InsertWord(word, translation, random_str);
    }
}

const std::vector<std::string>& TextProcessor::word_list() {
    if (!need_sort_) {
        return word_list_;
    }
    std::sort(word_list_.begin(), word_list_.end(), [](const std::string& s1, const std::string& s2) {
        if (s1.size() == s2.size()) {
            return s1 < s2;
        }
        return s1.size() > s2.size();
    });
    need_sort_ = false;
    return word_list_;
}

}  // namespace processor
}  // namespace gal
