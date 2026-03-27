                                        # Step 13: walkdirs, walkfiles, files, dirs
                                            def walkdirs(self):
                                                """Yield Path objects for all directories recursively."""
                                                for dirpath, dirnames, _ in os.walk(self):
                                                    for dirname in dirnames:
                                                        yield self.__class__(os.path.join(dirpath, dirname))

                                            def walkfiles(self, pattern=None):
                                                """Yield Path objects for all files recursively, optionally matching a pattern."""
                                                for dirpath, _, filenames in os.walk(self):
                                                    for filename in filenames:
                                                        p = self.__class__(os.path.join(dirpath, filename))
                                                        if pattern is None or fnmatch.fnmatch(filename, pattern):
                                                            yield p

                                            def files(self, pattern=None):
                                                """Yield Path objects for files in the current directory, optionally matching a pattern."""
                                                if not self.is_dir():
                                                    return
                                                for entry in os.listdir(self):
                                                    p = self.__class__(os.path.join(self, entry))
                                                    if p.is_file() and (pattern is None or fnmatch.fnmatch(entry, pattern)):
                                                        yield p

                                            def dirs(self, pattern=None):
                                                """Yield Path objects for directories in the current directory, optionally matching a pattern."""
                                                if not self.is_dir():
                                                    return
                                                for entry in os.listdir(self):
                                                    p = self.__class__(os.path.join(self, entry))
                                                    if p.is_dir() and (pattern is None or fnmatch.fnmatch(entry, pattern)):
                                                        yield p
                                        def hardlink_to(self, dst):
                                            os.link(self, dst)
                                            return Path(dst)

                                        def readlink(self):
                                            return Path(os.readlink(self))

                                        def walk(self):
                                            for dirpath, dirnames, filenames in os.walk(self):
                                                yield Path(dirpath)
                                                for name in dirnames + filenames:
                                                    yield Path(os.path.join(dirpath, name))
                                    def copytree(self, dst):
                                        import shutil
                                        shutil.copytree(self, dst)
                                        return Path(dst)

                                    def move(self, dst):
                                        import shutil
                                        shutil.move(self, dst)
                                        return Path(dst)

                                    def symlink(self, dst):
                                        os.symlink(self, dst)
                                        return Path(dst)
                                def rmdir_p(self):
                                    try:
                                        os.rmdir(self)
                                    except (FileNotFoundError, OSError):
                                        pass
                                    return self

                                def removedirs(self):
                                    os.removedirs(self)
                                    return self

                                def copy(self, dst):
                                    import shutil
                                    shutil.copy2(self, dst)
                                    return Path(dst)
                            def makedirs(self, exist_ok=True):
                                os.makedirs(self, exist_ok=exist_ok)
                                return self

                            def rmdir(self):
                                os.rmdir(self)
                                return self

                            def remove(self):
                                os.remove(self)
                                return self
                        def with_name(self, name):
                            return self.parent / name

                        def with_suffix(self, suffix):
                            base = self.stem + suffix
                            return self.parent / base

                        def touch(self):
                            with open(self, 'a'):
                                os.utime(self, None)
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
