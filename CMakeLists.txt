cmake_minimum_required(VERSION 3.5)

project(test)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

set(SOURCE_DIR      ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(BUILD_DIR       ${CMAKE_CURRENT_SOURCE_DIR}/build)
set(THIRD_PARTY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/third_party)

#------------------build submodule------------------#
# glog
add_subdirectory(third_party/glog)
set(GLOG_INCLUDE_DIR    ${THIRD_PARTY_DIR}/glog/src/glog)
set(GLOG_LIB_DIR        ${BUILD_DIR}/third_party/glog)
file(GLOB GLOG_LIB
    ${GLOG_LIB_DIR}/libglog.so
    ${GLOG_LIB_DIR}/libglog.so.0.7.0
    ${GLOG_LIB_DIR}/libglog.so.1)
# yaml-cpp
if(CMAKE_HOST_SYSTEM_NAME MATCHES "Windows")
    set(YAML_BUILD_SHARED_LIBS on)
    add_subdirectory(third_party/yaml-cpp)
endif() 

add_subdirectory(third_party/TransInterface)


#------------------build submodule------------------#




include_directories(
    ${SOURCE_DIR}
    ${THIRD_PARTY_DIR}/TransInterface/include/
    ${GLOG_INCLUDE_DIR}
   # ${THIRD_PARTY_DIR}/yaml-cpp/include/
    )

file(GLOB GAL_SRC
    ${SOURCE_DIR}/translate/machine_translator.cpp
    ${SOURCE_DIR}/translate/tencent_trans.cpp
    ${SOURCE_DIR}/processor/text_processor.cpp
    ${SOURCE_DIR}/processor/text_analyzer.cpp
    ${SOURCE_DIR}/gal_translator.cpp)

if(CMAKE_HOST_SYSTEM_NAME MATCHES "Linux")
    message(STATUS "Linux Compiling...")
    file(GLOB GAL_LIB
        ${THIRD_PARTY_DIR}/TransInterface/libGoInterface.so)
elseif(CMAKE_HOST_SYSTEM_NAME MATCHES "Windows")
    message(STATUS "Windows Compiling...")
    file(GLOB GAL_LIB
        ${THIRD_PARTY_DIR}/TransInterface/libGoInterface.dll
        ${THIRD_PARTY_DIR}/yaml-cpp/libyaml-cpp.dll)
else()
    message(ERROR "Unknown Platform...")
endif() 

add_executable(${PROJECT_NAME} 
    ${SOURCE_DIR}/gal.cpp
    ${GAL_SRC}
)

target_link_libraries(${PROJECT_NAME}
    ${GAL_LIB}
    ${GLOG_LIB}
    yaml-cpp
)
