cmake_minimum_required(VERSION 3.5)

project(test)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

#------------------build submodule------------------#
add_subdirectory(third_party/TransInterface)
set(YAML_BUILD_SHARED_LIBS on)
add_subdirectory(third_party/yaml-cpp)


#------------------build submodule------------------#


set(SOURCE_DIR      ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(THIRD_PARTY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/third_party)

include_directories(
    ${SOURCE_DIR}
    ${THIRD_PARTY_DIR}/TransInterface/include/
   # ${THIRD_PARTY_DIR}/yaml-cpp/include/
    )

file(GLOB GAL_SRC
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
    yaml-cpp
)
