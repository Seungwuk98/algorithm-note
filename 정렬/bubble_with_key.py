def bubble_sort(arr: list, key=None, cmp=None):
    ret = arr[:]
    n = len(ret)
    if key == None:
        def key(x): return x
    if cmp == None:
        def cmp(x, y):
            return x < y
    for i in range(n - 1):
        for j in range(n - i - 1):
            if cmp(key(ret[j+1]), key(ret[j])):
                ret[j], ret[j+1] = ret[j+1], ret[j]
    return ret
