#include <string>
#include <vector>

namespace gal {
namespace utils {

static void Replace(std::string* text, const std::string& old_str, const std::string& new_str) {
    if (!text) {
        return;
    }
    int32_t pos = static_cast<int32_t>(text->find(old_str));
    int32_t old_len = static_cast<int32_t>(old_str.size());
    while (pos >= 0) {
        *text = text->replace(pos, old_len, new_str);
        pos = text->find(old_str);
    }
}

static std::vector<std::string> Split(
    const std::string& text, const std::string& split_str, bool reserve_split_str = false) {
    std::vector<std::string> res;
    int32_t pre = 0;
    int32_t pos = static_cast<int32_t>(text.find(split_str, pre));
    while (pos >= 0) {
        res.push_back(text.substr(pre, pos - pre));
        if (reserve_split_str) {
            res.push_back(split_str);
        }
        pre = pos + split_str.size();
        pos = static_cast<int32_t>(text.find(split_str, pre));
    }
    if (pre < text.size()) {
        res.push_back(text.substr(pre, text.size() - pre));
    }
    if (res.empty()) {
        res.push_back(text);
    }
    return res;
}

}  // namespace utils
}  // namespace gal
