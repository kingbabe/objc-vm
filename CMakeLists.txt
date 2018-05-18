cmake_minimum_required(VERSION 3.9)
project(objc_vm_build)

set(CMAKE_CXX_STANDARD 11)

add_executable(objc_vm_build main.cpp objc_definition.h)