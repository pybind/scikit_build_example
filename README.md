scikit_build_example
==============

[![Gitter][gitter-badge]][gitter-link]

|      CI              | status |
|----------------------|--------|
| conda.recipe         | [![Conda Actions Status][actions-conda-badge]][actions-conda-link] |
| pip builds           | [![Pip Actions Status][actions-pip-badge]][actions-pip-link] |



An example project built with [pybind11](https://github.com/pybind/pybind11) and scikit-build. Python 3.6+ (see older commits for older versions of Python).


[gitter-badge]:            https://badges.gitter.im/pybind/Lobby.svg
[gitter-link]:             https://gitter.im/pybind/Lobby
[actions-badge]:           https://github.com/pybind/scikit_build_example/workflows/Tests/badge.svg
[actions-conda-link]:      https://github.com/pybind/scikit_build_example/actions?query=workflow%3AConda
[actions-conda-badge]:     https://github.com/pybind/scikit_build_example/workflows/Conda/badge.svg
[actions-pip-link]:        https://github.com/pybind/scikit_build_example/actions?query=workflow%3APip
[actions-pip-badge]:       https://github.com/pybind/scikit_build_example/workflows/Pip/badge.svg
[actions-wheels-link]:     https://github.com/pybind/scikit_build_example/actions?query=workflow%3AWheels
[actions-wheels-badge]:    https://github.com/pybind/scikit_build_example/workflows/Wheels/badge.svg

Installation
------------

- clone this repository
- `pip install ./scikit_build_example`


CI Examples
-----------

There are examples for CI in `.github/workflows`. A simple way to produces
binary "wheels" for all platforms is illustrated in the "wheels.yml" file,
using [`cibuildwheel`][].

License
-------

pybind11 is provided under a BSD-style license that can be found in the LICENSE
file. By using, distributing, or contributing to this project, you agree to the
terms and conditions of this license.

Test call
---------

```python
import scikit_build_example
scikit_build_example.add(1, 2)
```

[`cibuildwheel`]:          https://cibuildwheel.readthedocs.io

Explanations
------------

_Structure of this repository, concerning the package building_

````
.
├── CMakeLists.txt                   # Builds a native python module named "_core" whose source is in main.cpp
├── src/
│         ├── main.cpp               # Example of published functions (add, susbstract), which end up in the "_core" module
│         │
│         └── scikit_build_example/  #  A standard python package named "scikit_build_example" which imports   
│             └── __init__.py        # "_core" functions and publishes them
│             │
│             └── __init__.pyi       #  (Optional, not present in this repo). You could add a stub file here
│             │                      # in order to help users and to provide autocomplete inside IDEs.
│             │
│             └──_core.cpython-XX.so #  _core module location in pip editable mode (not committed in this repo) 
|                                    #  (appears only after building the module)
|
├── pyproject.toml                   # Standard setuptools config. Add you build requirements here
├── setup.py                         # Standard setuptools config. 
├── _skbuild/                        # Temp build directory used by pip (mentioned in .gitignore)
````

_Structure inside site-packages after installation (`pip install .`)_
````
venv/lib/python3.XX/site-packages/scikit_build_example/
├── __init__.py
└── _core.cpython-XX.so*
````

_Note about cmake install path_

`setup.py`, specifies `cmake_install_dir="src/scikit_build_example"`, and `CMakeLists.txt`specifies 
`install(TARGETS _core DESTINATION .)` so that the _core module final location will be `src/scikit_build_example/`


_Other elements in this repository_

````
├── docs/...                       # python_example documentation created by sphinx-quickstart
├── tests/...                      # A simple test
├── noxfile.py                     # Test runner and linter
|
├── conda.recipe/                  # Conda
│         └── meta.yaml
.github                            # Continuous integrations updates dependencies, and builds pip, wheels, and conda packages
├── dependabot.yml
└── workflows/ 
│    ├── conda.yml
│    ├── pip.yml
│    └── wheels.yml
````
