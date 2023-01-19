#include "machine_translator.h"

#include <iostream>
#include <yaml-cpp/yaml.h>

#include "tencent_trans.h"

using std::cout;
using std::endl;

namespace gal {
namespace trans {

MachineTranslator::MachineTranslator() {}

void MachineTranslator::LoadConfig(const std::string& config_path) {
    YAML::Node machine_translator = YAML::LoadFile(config_path);
    machine_translator = machine_translator["machine_translator"];
    if (!machine_translator.IsSequence()) {
        cout << "Fail to load machine_translator!" << endl;
    }
    for (int i = 0; i < machine_translator.size(); ++i) {
        YAML::Node translator = machine_translator[i];
        if (translator["translator"].as<std::string>() == "tencent") {
            TencentTrans* tencent_trans = new TencentTrans();
            std::string secret_id = translator["secret_id"].as<std::string>();
            std::string secret_key = translator["secret_key"].as<std::string>();
            double trans_freq = translator["trans_freq"].as<double>();
            tencent_trans->Init(secret_id, secret_key);
            tencent_trans->SetRegion();
            tencent_trans->SetLanguage("zh", "jp");
            translator_map_["tencent"] = tencent_trans;
        }
        // else if
        // else if
    }
}

void MachineTranslator::SetTranslator(const std::string& translator) {
    if (translator_map_.count(translator) != 0) {
        cur_translator_ = translator_map_[translator];
    } else {
        cur_translator_ = nullptr;
    }
}

std::string MachineTranslator::Translate(const std::string& src_text) {
    if (!cur_translator_) {
        return "error";
    }
    return cur_translator_->Translate(src_text);
}

}  // namespace trans
}  // namespace gal
