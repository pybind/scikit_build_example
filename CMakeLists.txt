cmake_minimum_required(VERSION 3.18)

project(scikit_build_example VERSION "0.0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

# Currently, Scikit-build does not support FindPython, so we convert the
# provided hints ourselves.
if(SKBUILD)
  set(Python_EXECUTABLE "${PYTHON_EXECUTABLE}")
  set(Python_INCLUDE_DIR "${PYTHON_INCLUDE_DIR}")
  set(Python_LIBRARY "${PYTHON_LIBRARY}")
endif()

set(Python_FIND_IMPLEMENTATIONS CPython PyPy)
find_package(Python REQUIRED COMPONENTS Interpreter Development)

# Scikit-Build does not add your site-packages to the search path automatically,
# so we need to add it here.
execute_process(
  COMMAND
    "${Python_EXECUTABLE}" -c
    "import skbuild, os; print(os.path.dirname(os.path.dirname(skbuild.__file__)))"
  OUTPUT_VARIABLE _tmp_sitepackages
  OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT ECHO_OUTPUT_VARIABLE
  ECHO_ERROR_VARIABLE)
list(APPEND CMAKE_PREFIX_PATH "${_tmp_sitepackages}")

# Now we can find pybind11
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE src/main.cpp)

target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS _core DESTINATION .)
