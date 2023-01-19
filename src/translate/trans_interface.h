#pragma once

#include <string>

namespace gal {
namespace trans {

class TransInterface {
public:
    virtual std::string Translate(const std::string& src_text) = 0;
};

}  // namespace trans
}  // namespace gal