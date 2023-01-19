#pragma once
#include <regex>
#include <vector>
#include <unordered_set>
#include <unordered_map>

namespace gal {
namespace processor {

struct AnalyzerRes {
    bool need_tranlate;
    std::string text;
};

class TextAnalyzer {
public:
    TextAnalyzer();

    void SetNewlineCharacter(const std::string& newline_character);

    void AddNewlineCharacterTrigger(const std::string& newline_character_trigger);

    void AddRegex(const std::string& regex_str);

    void AddSeparator(const std::string& separator, const std::string& translation = "");

    std::vector<AnalyzerRes> Analyze(const std::string& text);

private:
    bool NeedTranslate(std::string* text);

    void SplitTextByNewlineCharacter(std::vector<AnalyzerRes>* analyzer_res, const std::string& text);

    void SplitText(std::vector<AnalyzerRes>* text_vec, const std::string& separator, const std::string& translation);

private:
    std::string newline_character_;
    std::unordered_set<std::string> newline_character_trigger_;
    std::unordered_set<std::string> regex_vec_;
    std::unordered_map<std::string, std::string> separator_;
};

}  // namespace processor
}  // namespace gal
