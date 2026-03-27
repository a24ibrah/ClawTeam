                                        # Step 15: TempDir context manager, SpecialResolver, platform-specific helpers
                                        import tempfile
                                        import sys

                                        class TempDir:
                                            """Context manager for temporary directories."""
                                            def __enter__(self):
                                                self.dir = tempfile.TemporaryDirectory()
                                                return self.dir.name
                                            def __exit__(self, exc_type, exc_val, exc_tb):
                                                self.dir.cleanup()

                                        class SpecialResolver:
                                            """Platform-specific config/data directory resolver."""
                                            @staticmethod
                                            def config_dir():
                                                if sys.platform == 'win32':
                                                    return os.environ.get('APPDATA', os.path.expanduser('~'))
                                                elif sys.platform == 'darwin':
                                                    return os.path.expanduser('~/Library/Application Support')
                                                else:
                                                    return os.environ.get('XDG_CONFIG_HOME', os.path.expanduser('~/.config'))

                                            @staticmethod
                                            def data_dir():
                                                if sys.platform == 'win32':
                                                    return os.environ.get('LOCALAPPDATA', os.path.expanduser('~'))
                                                elif sys.platform == 'darwin':
                                                    return os.path.expanduser('~/Library/Application Support')
                                                else:
                                                    return os.environ.get('XDG_DATA_HOME', os.path.expanduser('~/.local/share'))

                                        def symlink_supported():
                                            """Return True if symlinks are supported on this platform."""
                                            if hasattr(os, 'symlink'):
                                                if sys.platform == 'win32':
                                                    import ctypes
                                                    return ctypes.windll.shell32.IsUserAnAdmin() != 0
                                                return True
                                            return False

                                        def path_separator():
                                            """Return the path separator for the current platform."""
                                            return os.sep
                                        # Step 14: glob/iglob enhancements, read_md5, read_hash, read_hexhash
                                            def glob(self, pattern):
                                                """Yield Path objects matching the pattern in the directory (supports recursive patterns)."""
                                                import glob as globmod
                                                for p in globmod.glob(os.path.join(self, pattern), recursive=True):
                                                    yield self.__class__(p)

                                            def iglob(self, pattern):
                                                """Yield Path objects matching the pattern in the directory (iterator, supports recursive patterns)."""
                                                import glob as globmod
                                                for p in globmod.iglob(os.path.join(self, pattern), recursive=True):
                                                    yield self.__class__(p)

                                            def read_md5(self):
                                                """Return the MD5 hash of the file contents."""
                                                import hashlib
                                                with open(self, 'rb') as f:
                                                    return hashlib.md5(f.read()).hexdigest()

                                            def read_hash(self, algo):
                                                """Return the hash (e.g., sha256) of the file contents using the specified algorithm."""
                                                import hashlib
                                                h = hashlib.new(algo)
                                                with open(self, 'rb') as f:
                                                    h.update(f.read())
                                                return h.digest()

                                            def read_hexhash(self, algo):
                                                """Return the hexadecimal hash string of the file contents using the specified algorithm."""
                                                import hashlib
                                                h = hashlib.new(algo)
                                                with open(self, 'rb') as f:
                                                    h.update(f.read())
                                                return h.hexdigest()
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
