cmake_minimum_required(VERSION 3.21)
project(HelloQml VERSION 1.0 LANGUAGES CXX)

find_package(Qt6 6.8 REQUIRED COMPONENTS Quick)
qt_standard_project_setup(REQUIRES 6.8)

qt_add_executable(hello main.cpp)
qt_add_qml_module(hello
    URI HelloQml
    QML_FILES Main.qml
)
target_link_libraries(hello PRIVATE Qt6::Quick)
