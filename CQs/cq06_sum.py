"""Summing the elements of a list using different loops"""
__author__: str = "730715418"

def w_sum(vals: list[float]) -> float:
    total = 0.0
    i = 0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total
print(w_sum([1.1, 0.9, 1.0]))

def f_sum(vals: list[float]) -> float:
    total = 0.0
    for val in vals:
        total += val
    return total
print(f_sum([1.1, 0.9, 1.0]))

def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total
print(f_range_sum([1.1, 0.9, 1.0]))