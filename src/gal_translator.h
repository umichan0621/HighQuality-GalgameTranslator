#pragma once
#include <string>
#include <vector>
#include <processor/text_analyzer.h>
#include <processor/text_processor.h>
#include <translate/tencent_trans.h>

namespace gal {

class GalTranslator {
public:
    GalTranslator();

    void SetFile(const std::string& src_text_path);

    void LoadConfig(const std::string& config_path);

    void Translate();

private:
    void LoadTextAnalyzer(const std::string& config_path);

private:
    std::string src_text_path_;
    std::vector<std::string> src_text_vec_;

    processor::TextAnalyzer text_analyzer_;
    processor::TextProcessor text_processor_;
    trans::TencentTrans translator_;
};

}  // namespace gal
