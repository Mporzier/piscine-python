def ft_map(func, lst):
    newLst = []
    for i in lst:
        newLst.append(func(i))
    return (newLst)
