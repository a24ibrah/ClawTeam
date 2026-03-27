# ClawTeam Path Replica: Feature List

This document enumerates all 59 features implemented in the ClawTeam replica of the original `jaraco/path` project. Each feature is mapped to its corresponding method, property, or class, with a brief description.

---

## 1. Path Construction & Compatibility
1. Path class (subclass of str)
2. Path() (defaults to current directory)
3. Path.using_module(ntpath)
4. String compatibility (join, print, etc.)

## 2. Path Operations
5. `/` operator (path joining)
6. .parent (parent directory)
7. .name (final component)
8. .suffix (file extension)
9. .stem (filename without extension)
10. .with_name(name)
11. .with_suffix(suffix)
12. .joinpath(*others)
13. .splitdrive()
14. .splitext()
15. .parts (tuple of path components)
16. .absolute() (absolute path)
17. .normpath() (normalize path)
18. .expand() (expand user/vars)
19. .expandvars() (expand environment variables)
20. .expanduser() (expand ~)

## 3. Filesystem Queries
21. .exists() (path exists)
22. .is_file() (is file)
23. .is_dir() (is directory)
24. .stat() (os.stat result)
25. .lstat() (os.lstat result)
26. .getsize() (file size)
27. .ctime (creation time)
28. .mtime (modification time)
29. .permissions (file permissions)
30. .access(mode) (os.access)

## 4. Directory/File Operations
31. .mkdir(exist_ok=True)
32. .makedirs()
33. .rmdir()
34. .rmdir_p() (remove, ignore errors)
35. .removedirs()
36. .removedirs_p() (remove dirs recursively)
37. .touch() (create file)
38. .remove() (delete file)
39. .remove_p() (delete, ignore errors)
40. .copy(dst)
41. .copytree(dst)
42. .move(dst)
43. .symlink(dst)
44. .hardlink_to(dst)
45. .readlink()
46. .readlinkabs()

## 5. Directory Traversal & Globbing
47. .walk() (recursive walk)
48. .walkdirs() (yield directories recursively)
49. .walkfiles(pattern=None) (yield files recursively)
50. .glob(pattern) (pattern matching, recursive)
51. .iglob(pattern) (iterator, recursive)
52. .files(pattern=None) (files in directory)
53. .dirs(pattern=None) (dirs in directory)
54. .iterdir() (directory entries)

## 6. Hashing & Checksums
55. .read_md5() (MD5 hash)
56. .read_hash(algo) (arbitrary hash)
57. .read_hexhash(algo) (hexadecimal hash)

## 7. Context Managers & Platform Helpers
58. TempDir context manager (temporary directories)
59. SpecialResolver (platform-specific config/data dirs)

---

**Note:** All features have been implemented and verified to match the original `jaraco/path` API and behavior as closely as possible. For details, see the implementation and verification logs.
