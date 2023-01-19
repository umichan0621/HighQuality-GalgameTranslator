#pragma once

#include <chrono>
#include <vector>
#include <unordered_map>

#include <utils/analyzer_res.h>

#include "trans_interface.h"

namespace gal {
namespace trans {

class MachineTranslator {
public:
    MachineTranslator();

    void LoadConfig(const std::string& config_path);

    void SetTranslator(const std::string& translator);

    std::string Translate(const std::string& src_text);

    std::string Translate(const std::vector<utils::AnalyzerRes>& analyzer_res);

private:
    std::chrono::high_resolution_clock::time_point last_translate_time_;
    std::chrono::milliseconds sleep_time_;
    TransInterface* cur_translator_;
    std::unordered_map<std::string, TransInterface*> translator_map_;
};
}  // namespace trans
}  // namespace gal
