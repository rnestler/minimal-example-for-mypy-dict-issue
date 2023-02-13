this_is_fine = {
    "bar": True,
    "value_0": 1.0,
    "value_1": 2.0,
}

this_is_not = {
    "bar": True,
    **{f"value_{n}": float(n) for n in range(2)},
}
