#include <unordered_map>
#include <string>
#include <vector>

namespace gal {
namespace processor {

using Dict = std::unordered_map<std::string, std::string>;

class TextProcessor {
public:
    TextProcessor();

private:
    Dict src_tmp_dic;
    Dict tmp_des_dic;
    Dict des_tmp_dic;
    std::vector<std::string> src_list;
};

}  // namespace processor
}  // namespace gal
