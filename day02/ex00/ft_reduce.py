def ft_reduce(func, lst):
    while len(lst) != 1:
        tmp = func(lst[0], lst[1])
        lst.pop(0)
        lst.insert(0, tmp)
        lst.pop(1)
    return lst[0]
