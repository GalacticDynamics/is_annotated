<h1 align='center'> <code>is_annotated</code> </h1>
<h2 align="center">Check if an object is an <code>Annotated</code> type.</h2>

This is a micro-package, containing the single function `isannotated` to check
if a type hint is an `Annotated` type. `Annotated` objects can't be checked by
normal `isinstance` checks.

## Installation

[![PyPI platforms][pypi-platforms]][pypi-link]
[![PyPI version][pypi-version]][pypi-link]

```bash
pip install is_annotated
```

## Documentation

[![Actions Status][actions-badge]][actions-link]

```python
from typing import Annotated
from is_annotated import isannotated

print(isannotated(1))
# False

print(isannotated(int))
# False

print(isannotated(Annotated[int, "1"]))
# True
```

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/GalacticDynamics/is_annotated/workflows/CI/badge.svg
[actions-link]:             https://github.com/GalacticDynamics/is_annotated/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/is_annotated
[conda-link]:               https://github.com/conda-forge/is_annotated-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/GalacticDynamics/is_annotated/discussions
[pypi-link]:                https://pypi.org/project/is_annotated/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/is_annotated
[pypi-version]:             https://img.shields.io/pypi/v/is_annotated

<!-- prettier-ignore-end -->
