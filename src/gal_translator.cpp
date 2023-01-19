#include "gal_translator.h"

#include <iostream>
#include <yaml-cpp/yaml.h>

#include <utils/file.hpp>

namespace gal {

GalTranslator::GalTranslator() {}

void GalTranslator::SetFile(const std::string& src_text_path) { src_text_path_ = src_text_path; }

void GalTranslator::LoadConfig(const std::string& config_path) {
    LoadTextAnalyzer(config_path + "text_analyzer.yaml");
    LoadCharacterName(config_path + "character_name.yaml");
}

void GalTranslator::Translate() {}

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
        std::cout << separator_need_translate[i][0].as<std::string>() << " "
                  << separator_need_translate[i][1].as<std::string>() << std::endl;
    }
}

void GalTranslator::LoadCharacterName(const std::string& config_path) {}

}  // namespace gal
