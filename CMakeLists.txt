cmake_minimum_required(VERSION 3.27)
project(engine3d-nfd LANGUAGES C CXX)

build_library(
    DIRECTORIES src
)

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR} ${CMAKE_CURRENT_LIST_DIR}/engine3d-ndf)

install(TARGETS ${PROJECT_NAME})
