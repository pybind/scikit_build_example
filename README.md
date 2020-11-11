scikit_build_example
==============

[![Gitter][gitter-badge]][gitter-link]

|      CI              | status |
|----------------------|--------|
| conda.recipe         | [![Conda Actions Status][actions-conda-badge]][actions-conda-link] |
| pip builds           | [![Pip Actions Status][actions-pip-badge]][actions-pip-link] |



An example project built with [pybind11](https://github.com/pybind/pybind11) and scikit-build.



[gitter-badge]:            https://badges.gitter.im/pybind/Lobby.svg
[gitter-link]:             https://gitter.im/pybind/Lobby
[actions-badge]:           https://github.com/pybind/scikit_build_example/workflows/Tests/badge.svg
[actions-conda-link]:      https://github.com/pybind/scikit_build_example/actions?query=workflow%3A%22Conda
[actions-conda-badge]:     https://github.com/pybind/scikit_build_example/workflows/Conda/badge.svg
[actions-pip-link]:        https://github.com/pybind/scikit_build_example/actions?query=workflow%3A%22Pip
[actions-pip-badge]:       https://github.com/pybind/scikit_build_example/workflows/Pip/badge.svg
[actions-wheels-link]:     https://github.com/pybind/scikit_build_example/actions?query=workflow%3AWheels
[actions-wheels-badge]:    https://github.com/pybind/scikit_build_example/workflows/Wheels/badge.svg

Installation
------------

**On Unix (Linux, macOS)**

 - clone this repository
 - `pip install ./scikit_build_example`

**On Windows**

 - For Python 3.5+:
     - clone this repository
     - `pip install ./scikit_build_example`
 - For Python 2.7:
     - Pybind11 + Scikit-Build does not support Python 2.7 on Windows.

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
