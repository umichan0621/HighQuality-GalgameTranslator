cmake_minimum_required(VERSION 3.5)

project(test)

set(CMAKE_CXX_STANDARD 14)

# find_package(Python3 COMPONENTS Interpreter Development)

# if (${Python3_FOUND})
#     message (STATUS "Python3_INCLUDE_DIRS = ${Python3_INCLUDE_DIRS}")
#     message (STATUS "Python3_LIBRARIES = ${Python3_LIBRARIES}")
# else()
#     message (FATAL_ERROR "Python3 not found, please install it.")
# endif()

add_executable(${PROJECT_NAME} 
    test.cpp)

include_directories(${PROJECT_NAME}
    ${Python3_INCLUDE_DIRS})


target_link_libraries(${PROJECT_NAME}
    ${Python3_LIBRARIES}
    E:/HighQuality-GalgameTranslator/pkg/hello.dll
)

