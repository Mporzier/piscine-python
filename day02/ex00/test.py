from ft_filter import ft_filter
from functools import reduce


def myFunc(v1):
    if v1 > 2:
        return True
    return False


lst = [1, 2, 3, 4, 5]
print(ft_filter(myFunc, lst))
