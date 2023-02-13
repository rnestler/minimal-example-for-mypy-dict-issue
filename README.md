# Minimal example for-mypy dict issue

This is a minimal example to reproduce my issue in
https://github.com/python/mypy/issues/7339#issuecomment-1427805016

It is expected that mypy will successfully typecheck this code, but it fails
with:

```
test.py:12: error: Value expression in dictionary comprehension has incompatible type "float"; expected type "bool"  [misc]
test.py:23: error: Value expression in dictionary comprehension has incompatible type "float"; expected type "bool"  [misc]
Found 2 errors in 1 file (checked 1 source file)
```
