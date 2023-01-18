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

    void AddUnnecessaryNewlineCharacter(const std::string& unnecessary_newline_character);

    void AddRegex(const std::string& regex_str);

    void AddSeparator(const std::string& separator);

    void AddSeparatorNeedTranslate(const std::string& separator_need_translate, const std::string& translation);

    std::vector<AnalyzerRes> Analyze(const std::string& text);

private:
    bool NeedTranslate(std::string* text);
    // std::vector<std::string>

private:
    std::string newline_character_;
    std::unordered_set<std::string> unnecessary_newline_character_;
    std::unordered_set<std::string> regex_vec_;
    std::unordered_map<std::string, std::string> separator_;
};

}  // namespace processor
}  // namespace gal
