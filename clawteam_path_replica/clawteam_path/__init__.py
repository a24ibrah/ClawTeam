# clawteam_path/__init__.py

"""
ClawTeam-generated replica of jaraco/path: Path class and helpers
Implements the core Path class (subclass of str) for filesystem path manipulation.
API and design based on deep_breakdown.md and commit_history.csv
"""

import os
import sys
import shutil
import hashlib
from typing import Iterator, Any, Optional, Callable, ContextManager

class Path(str):
    """
    Replica of jaraco/path Path class (core API only, incremental features to be added).
    """
    def __new__(cls, *args, **kwargs):
        if len(args) == 0:
            value = os.curdir
        else:
            value = os.path.join(*args)
        return str.__new__(cls, value)

    def __truediv__(self, other):
        return Path(os.path.join(self, str(other)))

    @property
    def parent(self):
        return Path(os.path.dirname(self))

    @property
    def name(self):
        return os.path.basename(self)

    @property
    def suffix(self):
        base = self.name
        dot = base.rfind('.')
        return base[dot:] if dot != -1 else ''

    @property
    def stem(self):
        base = self.name
        dot = base.rfind('.')
        return base[:dot] if dot != -1 else base

    def exists(self):
        return os.path.exists(self)

    def is_file(self):
        return os.path.isfile(self)

    def is_dir(self):
        return os.path.isdir(self)

    def mkdir(self, exist_ok=True):
        os.makedirs(self, exist_ok=exist_ok)
        return self

    def iterdir(self):
        if not self.is_dir():
            raise NotADirectoryError(self)
        for entry in os.listdir(self):
            yield Path(self / entry)

    def joinpath(self, *others):
        return Path(self, *others)

    def absolute(self):
        return Path(os.path.abspath(self))

    def stat(self):
        return os.stat(self)

    def read_text(self, encoding=None):
        with open(self, encoding=encoding or 'utf-8') as f:
            return f.read()

    def write_text(self, data, encoding=None):
        with open(self, 'w', encoding=encoding or 'utf-8') as f:
            f.write(data)
        return self

    def read_bytes(self):
        with open(self, 'rb') as f:
            return f.read()

    def write_bytes(self, data):
        with open(self, 'wb') as f:
            f.write(data)
        return self

    def glob(self, pattern):
        import glob
        for match in glob.glob(os.path.join(self, pattern)):
            yield Path(match)

    def __repr__(self):
        return f"Path({super().__repr__()})"

# Additional helpers, context managers, and advanced features will be added incrementally.
