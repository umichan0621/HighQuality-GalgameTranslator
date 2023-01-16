cmake_minimum_required(VERSION 3.5)

project(test)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

set(SOURCE_DIR          ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(THIRD_PARTY_DIR     ${CMAKE_CURRENT_SOURCE_DIR}/third_party)
set(THIRD_PARTY_LIB     ${THIRD_PARTY_DIR}/lib)
set(THIRD_PARTY_INCLUDE ${THIRD_PARTY_DIR}/include)


include_directories(
    ${SOURCE_DIR}
    ${THIRD_PARTY_DIR}/GoInterface/include/
)

add_executable(${PROJECT_NAME} 
    ${SOURCE_DIR}/gal.cpp
    ${SOURCE_DIR}/translate/tencent_trans.cpp
    
)


target_link_libraries(${PROJECT_NAME}
    ${THIRD_PARTY_DIR}/GoInterface/lib/libGoInterface.dll
)

