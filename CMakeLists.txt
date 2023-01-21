cmake_minimum_required(VERSION 3.5)

project(test)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
add_definitions(-w)
set(SOURCE_DIR          ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(THIRD_PARTY_DIR     ${CMAKE_CURRENT_SOURCE_DIR}/third_party)
set(TARGET_DIR          ${CMAKE_CURRENT_SOURCE_DIR}/${PROJECT_NAME})
set(YAMLCPP_BUILD_DIR   ${THIRD_PARTY_DIR}/yaml-cpp/build)
set(GLOG_BUILD_DIR      ${THIRD_PARTY_DIR}/glog/build)

file(MAKE_DIRECTORY ${TARGET_DIR})

#------------------build submodule------------------#

if(CMAKE_HOST_SYSTEM_NAME MATCHES "Windows")
#--------------------build glog---------------------#
    if(EXISTS ${TARGET_DIR}/libglog.dll)
        message(STATUS "libglog.dll found,skip...")
    else()
        file(MAKE_DIRECTORY ${GLOG_BUILD_DIR})
        execute_process(
            COMMAND cmake -DCMAKE_INSTALL_PREFIX=${GLOG_BUILD_DIR} -DWITH_GFLAGS=off -DWITH_GTEST=off -DWITH_SYMBOLIZE=off -DWITH_THREADS=off -DWITH_CUSTOM_PREFIX=on -G "MinGW Makefiles" ..
            WORKING_DIRECTORY ${GLOG_BUILD_DIR})
        execute_process(
            COMMAND mingw32-make install --no-print-directory -j8
            WORKING_DIRECTORY ${GLOG_BUILD_DIR})
        file(COPY ${GLOG_BUILD_DIR}/bin/libglog.dll DESTINATION ${TARGET_DIR})
    endif()
    set(GLOG_INCLUDE ${GLOG_BUILD_DIR}/include)
    file(GLOB GLOG_LIB ${TARGET_DIR}/libglog.dll)

#------------------build yaml-cpp-------------------#
    if(EXISTS ${TARGET_DIR}/libyaml-cpp.dll)
        message(STATUS "libyaml-cpp.dll found,skip...")
    else()
        file(MAKE_DIRECTORY ${YAMLCPP_BUILD_DIR})
        execute_process(
            COMMAND cmake -DCMAKE_INSTALL_PREFIX=${YAMLCPP_BUILD_DIR} -DYAML_BUILD_SHARED_LIBS=on -G "MinGW Makefiles" ..
            WORKING_DIRECTORY ${YAMLCPP_BUILD_DIR})
        execute_process(
            COMMAND mingw32-make install --no-print-directory -j8
            WORKING_DIRECTORY ${YAMLCPP_BUILD_DIR})
        file(COPY ${YAMLCPP_BUILD_DIR}/bin/libyaml-cpp.dll DESTINATION ${TARGET_DIR})
    endif()
    file(GLOB YAMLCPP_LIB ${TARGET_DIR}/libyaml-cpp.dll)
    set(YAMLCPP_INCLUDE ${THIRD_PARTY_DIR}/yaml-cpp/include)

#----------------build GoInterface-----------------#
    if(EXISTS ${TARGET_DIR}/libGoInterface.dll)
        message(STATUS "libGoInterface.dll found,skip...")
    else()
        file(COPY ${THIRD_PARTY_DIR}/TransInterface/libGoInterface.dll DESTINATION ${TARGET_DIR})
    endif()
    set(GOINTERFACE_INCLUDE ${THIRD_PARTY_DIR}/TransInterface/include)
    file(GLOB GOINTERFACE_LIB ${TARGET_DIR}/libGoInterface.dll)
elseif(CMAKE_HOST_SYSTEM_NAME MATCHES "Linux")

else()
    message(ERROR "Unknown Platform...")
endif()

#------------------build submodule------------------#

include_directories(
    ${SOURCE_DIR}
    ${GOINTERFACE_INCLUDE}
    ${GLOG_INCLUDE}
    ${YAMLCPP_INCLUDE}
)

file(GLOB GAL_SRC
    ${SOURCE_DIR}/translate/machine_translator.cpp
    ${SOURCE_DIR}/translate/tencent_trans.cpp
    ${SOURCE_DIR}/processor/text_processor.cpp
    ${SOURCE_DIR}/processor/text_analyzer.cpp
    ${SOURCE_DIR}/gal_translator.cpp)

add_executable(${PROJECT_NAME} 
    ${SOURCE_DIR}/gal.cpp
    ${GAL_SRC}
)

target_link_libraries(${PROJECT_NAME}
    ${GAL_LIB}
    ${GLOG_LIB}
    ${GOINTERFACE_LIB}
    ${YAMLCPP_LIB})

install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${TARGET_DIR}
)
