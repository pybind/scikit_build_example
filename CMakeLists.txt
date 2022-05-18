cmake_minimum_required(VERSION 3.15...3.22)

project(scikit_build_example VERSION "0.0.1")

#
# Add pybind11:
# 1/ Either by adding it to pyproject.toml build-system/requires
# 2/ Either by adding it as a submodule
#

# 1/ Here, we find pybind11 via python, using pyproject.toml build-system/requires
# (this will work when running `pip install`, but not in a standard cmake build)
if(SKBUILD)
  # Scikit-Build does not add your site-packages to the search path
  # automatically, so we need to add it _or_ the pybind11 specific directory
  # here.
  execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c
            "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE _tmp_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
  list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
endif()
# Now we can find pybind11
find_package(pybind11 CONFIG REQUIRED)

# 2/ As an alternative, we could also add pybind11 by pointing to a submodule somewhere in the repository
#   (This would work for `pip install` and for regular cmake builds)
# add_subdirectory(path/to/pybind11)

#
# Add our _core native module (which will be wrapped in a standard python package, see src/scikit_build_example/__init__.py)
#
pybind11_add_module(_core MODULE src/main.cpp)
target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

#
# Installation
#
# Note about install paths:
# `setup.py`, specifies `cmake_install_dir="src/scikit_build_example"`, so that the _core module final location
# will be `src/scikit_build_example/./`
install(TARGETS _core DESTINATION .)

#
# Optional, for pip editable mode, copy the module to src/scikit_build_example/ after each build
# (so that modifications are usable without a full `pip install`
#
add_custom_command(
    TARGET _core
    POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    $<TARGET_FILE:_core>
    ${CMAKE_CURRENT_LIST_DIR}/src/scikit_build_example/$<TARGET_FILE_NAME:_core>
)
