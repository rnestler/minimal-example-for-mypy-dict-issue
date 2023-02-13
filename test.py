from collections import OrderedDict
from typing import Union

this_is_fine = {
    "bar": True,
    "value_0": 1.0,
    "value_1": 2.0,
}

this_is_not = {
    "bar": True,
    **{f"value_{n}": float(n) for n in range(2)},
}

this_is_ok_again: dict[str, Union[bool, float]] = {
    "bar": True,
    **{f"value_{n}": float(n) for n in range(2)},
}

MyOrderedDict = OrderedDict[str, Union[bool, float]]
but_this_not_ok_again: MyOrderedDict = MyOrderedDict({
    "bar": True,
    **{f"value_{n}": float(n) for n in range(2)},
})
