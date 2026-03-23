                def stat(self):
                    return os.stat(self)

                def read_text(self, encoding=None):
                    with open(self, encoding=encoding or 'utf-8') as f:
                        return f.read()

                def write_text(self, data, encoding=None):
                    with open(self, 'w', encoding=encoding or 'utf-8') as f:
                        f.write(data)
                    return self
            def iterdir(self):
                if not self.is_dir():
                    raise NotADirectoryError(self)
                for entry in os.listdir(self):
                    yield Path(os.path.join(self, entry))

            def joinpath(self, *others):
                return Path(os.path.join(self, *others))

            def absolute(self):
                return Path(os.path.abspath(self))
        def is_file(self):
            return os.path.isfile(self)

        def is_dir(self):
            return os.path.isdir(self)

        def mkdir(self, exist_ok=True):
            os.makedirs(self, exist_ok=exist_ok)
            return self
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
