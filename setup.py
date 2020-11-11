# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

setup(
    name="scikit_build_example",
    version="0.0.1",
    description="a minimal example package (with pybind11)",
    author="Henry Schreiner",
    license="MIT",
    packages=["scikit_build_example"],
    package_dir={"": "src"},
    cmake_install_dir="src/scikit_build_example",
)
