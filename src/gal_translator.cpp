#include "gal_translator.h"

#include <iostream>
#include <yaml-cpp/yaml.h>

#include <utils/file.hpp>
#include <utils/string.hpp>

using std::cout;
using std::endl;

namespace gal {

GalTranslator::GalTranslator() {}

void GalTranslator::SetFile(const std::string& src_text_path) {
    src_text_path_ = src_text_path;
    des_text_path_ = src_text_path;
    utils::ReplaceOnce(&des_text_path_, ".", "_zh.");
}

void GalTranslator::LoadConfig(const std::string& config_path) {
    LoadTextAnalyzer(config_path + "text_analyzer.yaml");
    LoadCharacterName(config_path + "character_name.yaml");
    translator_.LoadConfig(config_path + "config.yaml");
    translator_.SetTranslator("tencent");
}

void GalTranslator::Translate() {
    if (!utils::FileExists(src_text_path_)) {
        cout << "File " << src_text_path_ << " not exists..." << endl;
        return;
    }
    std::vector<std::string> src_text_vec;
    if (!utils::ReadFile(src_text_path_, &src_text_vec)) {
        cout << "Fail to load file  " << src_text_path_ << "..." << endl;
        return;
    }

    int32_t complete_line;
    if (!utils::FileExists(des_text_path_)) {
        complete_line = 0;
    } else {
        complete_line = utils::FileLineCount(des_text_path_);
    }

    // for (int32_t i = complete_line; i < complete_line + 10; ++i) {
    //     std::string des_text = src_text_vec[i];

    //     auto x = text_analyzer_.Analyze(des_text);

    //     for (auto z : x) {
    //         cout << z.need_tranlate << " " << z.text << endl;
    //     }

    //     cout << des_text << "  |  ";
    //     des_text = translator_.Translate(x);
    //     cout << des_text << endl;

    //     cout << "------------------------------------" << endl;
    //     if (i > 0) {
    //         des_text = "\n" + des_text;
    //     }
    //     utils::WriteFileAppend(des_text_path_, des_text);
    // }
}

void GalTranslator::LoadTextAnalyzer(const std::string& config_path) {
    // Load text analyzer
    YAML::Node text_analyzer = YAML::LoadFile(config_path);
    text_analyzer = text_analyzer["text_analyzer"];
    // newline_character
    text_analyzer_.SetNewlineCharacter(text_analyzer["newline_character"].as<std::string>());
    // newline_character_trigger
    YAML::Node newline_character_trigger = text_analyzer["newline_character_trigger"];
    if (!newline_character_trigger.IsSequence()) {
        std::cout << "Fail to load newline_character_trigger" << std::endl;
    }
    for (int i = 0; i < newline_character_trigger.size(); ++i) {
        text_analyzer_.AddNewlineCharacterTrigger(newline_character_trigger[i].as<std::string>());
    }
    // regular_expression
    YAML::Node regular_expression = text_analyzer["regular_expression"];
    if (!regular_expression.IsSequence()) {
        std::cout << "Fail to load regular_expression" << std::endl;
    }
    for (int i = 0; i < regular_expression.size(); ++i) {
        text_analyzer_.AddRegex(regular_expression[i].as<std::string>());
    }
    // separator
    YAML::Node separator = text_analyzer["separator"];
    if (!separator.IsSequence()) {
        std::cout << "Fail to load separator" << std::endl;
    }
    for (int i = 0; i < separator.size(); ++i) {
        text_analyzer_.AddSeparator(separator[i].as<std::string>());
    }
    // separator_need_translate
    YAML::Node separator_need_translate = text_analyzer["separator_need_translate"];
    if (!separator_need_translate.IsSequence()) {
        std::cout << "Fail to load separator_need_translate" << std::endl;
    }
    for (int i = 0; i < separator_need_translate.size(); ++i) {
        if (!separator_need_translate[i].IsSequence() || separator_need_translate[i].size() != 2) {
            std::cout << "Fail to load separator_need_translate, line " << i + 1 << std::endl;
        }
        text_analyzer_.AddSeparator(
            separator_need_translate[i][0].as<std::string>(), separator_need_translate[i][1].as<std::string>());
    }
}

void GalTranslator::LoadCharacterName(const std::string& config_path) {
    YAML::Node character_name_list = YAML::LoadFile(config_path);
    YAML::Node common_process = character_name_list["common_process"];
    if (!common_process.IsSequence()) {
        std::cout << "Fail to load common_process" << std::endl;
    }
    std::vector<processor::NameProcess> common_name_process;
    for (int i = 0; i < common_process.size(); ++i) {
        YAML::Node process = common_process[i];
        processor::NameProcess name_process;
        name_process.is_first_name = process["is_first_name"].as<bool>();
        name_process.is_tail = process["is_tail"].as<bool>();
        name_process.is_translation_tail = process["is_translation_tail"].as<bool>();
        name_process.word = process["word"].as<std::string>();
        name_process.translation = process["translation"].as<std::string>();
        common_name_process.emplace_back(name_process);
    }

    character_name_list = character_name_list["character_name_list"];
    if (!character_name_list.IsSequence()) {
        std::cout << "Fail to load character_name_list" << std::endl;
        return;
    }
    for (int i = 0; i < character_name_list.size(); ++i) {
        YAML::Node character = character_name_list[i];
        processor::GalCharacter gal_character;
        gal_character.first_name = character["first_name"].as<std::string>();
        gal_character.first_name_translation = character["first_name_translation"].as<std::string>();
        gal_character.last_name = character["last_name"].as<std::string>();
        gal_character.last_name_translation = character["last_name_translation"].as<std::string>();
        for (int j = 0; j < character["process"].size(); ++j) {
            YAML::Node process = character["process"][j];
            processor::NameProcess name_process;
            name_process.is_first_name = process["is_first_name"].as<bool>();
            name_process.is_tail = process["is_tail"].as<bool>();
            name_process.is_translation_tail = process["is_translation_tail"].as<bool>();
            name_process.word = process["word"].as<std::string>();
            name_process.translation = process["translation"].as<std::string>();
            gal_character.process_vec.emplace_back(name_process);
        }
        for (const auto& name_process : common_name_process) {
            gal_character.process_vec.emplace_back(name_process);
        }
        text_processor_.InsertCharacter(gal_character);
    }
}

}  // namespace gal
