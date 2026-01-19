cmake_minimum_required(VERSION 3.27)
project(demo LANGUAGES C CXX)

build_application(
    SOURCES application.cpp
    PACKAGES
    nfd

    LINK_PACKAGES
    nfd::nfd
)

