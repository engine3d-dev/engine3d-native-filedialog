cmake_minimum_required(VERSION 3.27)
project(demo LANGUAGES C CXX)

build_application(
    SOURCES application.cpp
    PACKAGES
    engine3d-nfd
    LINK_PACKAGES
    engine3d-nfd::engine3d-nfd
)

