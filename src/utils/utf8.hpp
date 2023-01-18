#pragma once
#include <wchar.h>
#include <windows.h>
#include <string>

namespace gal {
namespace utils {

static std::string string_to_utf8(const std::string& str_src) {
    int32_t len1 = ::MultiByteToWideChar(CP_ACP, 0, str_src.c_str(), -1, NULL, 0);

    wchar_t* pw_buf = new wchar_t[len1 + 1];  // 一定要加1，不然会出现尾巴
    ZeroMemory(pw_buf, len1 * 2 + 2);

    ::MultiByteToWideChar(CP_ACP, 0, str_src.c_str(), str_src.length(), pw_buf, len1);

    int Len2 = ::WideCharToMultiByte(CP_UTF8, 0, pw_buf, -1, NULL, NULL, NULL, NULL);

    char* p_buf = new char[Len2 + 1];
    ZeroMemory(p_buf, Len2 + 1);

    ::WideCharToMultiByte(CP_UTF8, 0, pw_buf, len1, p_buf, Len2, NULL, NULL);

    std::string str_des(p_buf);

    delete[] pw_buf;
    delete[] p_buf;

    pw_buf = NULL;
    p_buf = NULL;

    return str_des;
}

static std::string utf8_to_string(const std::string& str_src) {
    int32_t len1 = MultiByteToWideChar(CP_UTF8, 0, str_src.c_str(), -1, NULL, 0);

    wchar_t* pw_buf = new wchar_t[len1 + 1];  // 一定要加1，不然会出现尾巴
    memset(pw_buf, 0, len1 * 2 + 2);

    MultiByteToWideChar(CP_UTF8, 0, str_src.c_str(), str_src.length(), pw_buf, len1);

    int32_t Len2 = WideCharToMultiByte(CP_ACP, 0, pw_buf, -1, NULL, NULL, NULL, NULL);

    char* p_buf = new char[Len2 + 1];
    memset(p_buf, 0, Len2 + 1);

    WideCharToMultiByte(CP_ACP, 0, pw_buf, len1, p_buf, Len2, NULL, NULL);

    std::string str_des = p_buf;

    delete[] p_buf;
    delete[] pw_buf;

    p_buf = NULL;
    pw_buf = NULL;

    return str_des;
}

}  // namespace utils
}  // namespace gal
