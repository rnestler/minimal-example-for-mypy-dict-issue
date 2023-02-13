# Minimal example for-mypy dict issue

This is a minimal example to reproduce my issue in

The expected type for the dict is `dict[str, Union[bool, float]]`, but mypy
shows:

```
test.py:6: note: Revealed type is "builtins.dict[builtins.str, builtins.float]"
```
