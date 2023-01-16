#include "text_processor.h"
#include <time.h>

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

}  // namespace processor
}  // namespace gal