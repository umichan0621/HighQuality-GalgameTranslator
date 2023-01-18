#pragma once
#include <string>

namespace gal {
namespace trans {

class TencentTrans {
public:
    TencentTrans();

    void Init(const std::string& secret_id, const std::string& secret_key) {
        secret_id_ = secret_id;
        secret_key_ = secret_key;
    }

    void SetRegion(const std::string& region = "ap-shanghai") { region_ = region; }

    void SetLanguage(const std::string& des_language, const std::string& src_language = "jp") {
        des_language_ = des_language;
        src_language_ = src_language;
    }

    std::string Translate(const std::string& src_text);

private:
    std::string secret_id_;
    std::string secret_key_;
    std::string region_;
    std::string des_language_;
    std::string src_language_;
};

}  // namespace trans
}  // namespace gal
