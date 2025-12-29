
set(
    all_headers
    ../nfd/nfd.h
    ../nfd/nfd_common.h
    ../nfd/simple_exec.h
)

set(
    all_src
    nfd/nfd_common.cpp
)

if(WIN32)
    list(APPEND all_src nfd/nfd_win.cpp)
endif(WIN32)

if(APPLE)
    list(APPEND all_src nfd/cocoa.m)
endif(APPLE)

if(LINUX)
list(APPEND all_src nfd/nfd_gtk.cpp)
endif(LINUX)

add_library(${PROJECT_NAME} ${all_headers} ${all_src})
