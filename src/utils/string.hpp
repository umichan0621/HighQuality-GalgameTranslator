#include <string>

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

}  // namespace utils
}  // namespace gal
