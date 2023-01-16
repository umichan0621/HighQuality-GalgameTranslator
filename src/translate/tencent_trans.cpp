#include "tencent_trans.h"

#include <GoInterface.h>

namespace gal {
namespace trans {

TencentTrans::TencentTrans()
    : secret_id_(""), secret_key_(""), region_("ap-shanghai"), des_language_("zh"), src_language_("jp") {}

std::string TencentTrans::Translate(const std::string& src_text) {
    if (secret_id_.empty() || secret_key_.empty()) {
        return "error";
    }
    std::string res = TencentTranslate(            // Param
        const_cast<char*>(secret_id_.c_str()),     // SecretId
        const_cast<char*>(secret_key_.c_str()),    // SecretKey
        const_cast<char*>(region_.c_str()),        // Region: "ap-shanghai"
        const_cast<char*>(src_language_.c_str()),  // SrcLanguage: "jp"
        const_cast<char*>(des_language_.c_str()),  // DrcLanguage: "zh"
        const_cast<char*>(src_text.c_str()));      // SrcText: "Hello world"
    return res;
}

}  // namespace trans
}  // namespace gal
