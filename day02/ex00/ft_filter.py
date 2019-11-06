def ft_filter(func, lst):
    newLst = []
    for i in lst:
        if func(i):
            newLst.append(i)
    return (newLst)
