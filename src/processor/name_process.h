#pragma once
#include <string>
#include <vector>

namespace gal {
namespace processor {

struct NameProcess {
    bool is_tail = true;
    bool is_translation_tail = true;
    std::string word;
    std::string translation;
};

struct GalCharacter {
    std::string name;
    std::string translation;
    std::vector<NameProcess> process_vec;
};

}  // namespace processor
}  // namespace gal
