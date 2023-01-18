#pragma once
#include <fstream>
#include <string>
#include <vector>

namespace gal {
namespace utils {

static bool ReadFile(const std::string& path, std::vector<std::string>* content) {
    std::fstream fs;
    fs.open(path, std::ios::in);
    if (!fs.is_open()) {
        return false;
    }
    std::string temp;

    while (getline(fs, temp)) {
        content->emplace_back(temp);
    }
    fs.close();
    return true;
}

}  // namespace utils
}  // namespace gal
