#include <string>
#include <vector>

namespace gal {
namespace processor {

struct NameProcess {
    bool is_first_name = true;
    bool is_tail = true;
    bool is_translation_tail = true;
    std::string word;
    std::string translation;
};

struct GalName {
    std::string first_name;
    std::string first_name_translation;
    std::string last_name;
    std::string last_name_translation;
    std::vector<NameProcess> process_vec;
};

}  // namespace processor
}  // namespace gal
