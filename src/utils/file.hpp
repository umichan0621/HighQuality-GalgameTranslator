#pragma once
#include <fstream>
#include <string>
#include <vector>

namespace gal {
namespace utils {

static bool FileExists(const std::string& path) {
    std::ifstream ifs(path.c_str());
    return ifs.good();
}

static int32_t FileLineCount(const std::string& path) {
    std::fstream fs;
    fs.open(path, std::ios::in);
    if (!fs.is_open()) {
        return false;
    }
    int32_t count = 0;
    std::string temp;
    while (getline(fs, temp)) {
        ++count;
    }
    fs.close();
    return count;
}

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

static bool WriteFileAppend(const std::string& path, const std::string& content) {
    std::fstream fs;
    fs.open(path, std::ios::app);
    if (!fs.is_open()) {
        return false;
    }
    fs << content;
    return true;
}

}  // namespace utils
}  // namespace gal
