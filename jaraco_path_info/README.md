# jaraco/path Project Summary

## Overview
- **Project:** jaraco/path (formerly path.py)
- **Purpose:** Object-oriented file system path manipulation in Python
- **Key Feature:** Implements `Path` objects as first-class entities, allowing direct operations on files/paths
- **Similar to:** Python's pathlib, but with additional features and a longer history
- **Maintainer:** jaraco (Jason R. Coombs)
- **Language:** Python

## Features
- Path objects as subclasses of `str` (can be used directly as strings)
- Globbing: `d.files("*.py")` returns all Python files in a directory
- Context manager for changing working directory: `with Path("somewhere"): ...`
- Path concatenation with `/` operator
- Quality-of-life methods: `rmtree`, `remove_p`, `.permissions`, `walk`, `TempDir`, `chmod`
- Superior portability and subclassing compared to pathlib
- Designed to be a drop-in replacement for pathlib where possible

## Example Usage
```python
from path import Path

d = Path("/home/guido/bin")
for f in d.files("*.py"):
    f.chmod(0o755)

with Path("somewhere"):
    # cwd is now 'somewhere'
    ...

foo_txt = Path("bar") / "foo.txt"
```

## Advantages over pathlib
- Path objects are subclasses of `str` (no need to cast to string)
- Easier subclassing (no OS-specific subclasses needed)
- More utility methods and properties
- Faster iteration and improvement (not tied to stdlib release cycle)

## Project Structure
- `path/` (main code)
- `tests/` (unit tests)
- `docs/` (documentation)
- Standard Python project files: `pyproject.toml`, `README.rst`, etc.

## Resources
- [GitHub Repo](https://github.com/jaraco/path)
- [Documentation](https://path.readthedocs.io/)

---
This file summarizes the purpose, features, and structure of the jaraco/path project for experiment planning.
