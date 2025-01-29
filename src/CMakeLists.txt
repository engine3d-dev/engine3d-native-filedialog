
set(
    all_headers
    ../engine3d-nfd/nfd.h
    ../engine3d-nfd/nfd_common.h
    ../engine3d-nfd/simple_exec.h
)

set(
    all_src
    engine3d-nfd/nfd_common.c
)

if(WIN32)
    list(APPEND all_src engine3d-nfd/nfd_win.cpp)
endif(WIN32)

if(APPLE)
    list(APPEND all_src engine3d-nfd/cocoa.m)
endif(APPLE)

if(LINUX)
list(APPEND all_src engine3d-nfd/nfd_gtk.c)
endif(LINUX)

add_library(${PROJECT_NAME} ${all_headers} ${all_src})
