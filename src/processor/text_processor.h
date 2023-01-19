#pragma once
#include <unordered_map>
#include <string>
#include <vector>
#include <functional>

#include "name_process.h"

namespace gal {
namespace processor {

using str_func = std::function<std::string()>;

class TextProcessor {
    using Dict = std::unordered_map<std::string, std::string>;

public:
    TextProcessor();

    std::string Process(const std::string& text);

    std::string Recover(const std::string& text);

    void InsertWord(const std::string& word, const std::string& translation);

    void InsertWord(const std::string& word, const std::string& translation, str_func random_str);

    void InsertCharacter(const GalCharacter& gal_haracter);

    void InsertCharacter(const GalCharacter& gal_haracter, str_func random_str);

private:
    const std::vector<std::string>& word_list();

private:
    Dict word_tmp_dic_;
    Dict tmp_trans_dic_;
    Dict trans_tmp_dic_;
    std::vector<std::string> word_list_;
    bool need_sort_;
};

}  // namespace processor
}  // namespace gal
