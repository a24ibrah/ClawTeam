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
# ClawTeam Path Replica - Step 1
# Basic Path class skeleton (subclass of str) with minimal constructor and string compatibility.

import os

class Path(str):
    def __new__(cls, value=None):
        if value is None:
            value = "."
        return str.__new__(cls, value)

    def __truediv__(self, other):
        return Path(os.path.join(self, str(other)))

    @property
    def parent(self):
        return Path(os.path.dirname(self))

    @property
    def name(self):
        return os.path.basename(self)

    def __repr__(self):
        return f"Path({super().__repr__()})"
