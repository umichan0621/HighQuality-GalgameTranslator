#pragma once

#include <unordered_map>

#include "trans_interface.h"

namespace gal {
namespace trans {

class MachineTranslator {
public:
    MachineTranslator();

    void LoadConfig(const std::string& config_path);

    void SetTranslator(const std::string& translator);

    std::string Translate(const std::string& src_text);

private:
    int32_t trans_freq_;
    TransInterface* cur_translator_;
    std::unordered_map<std::string, TransInterface*> translator_map_;
};
}  // namespace trans
}  // namespace gal
