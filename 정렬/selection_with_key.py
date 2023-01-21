def selection_sort(arr: list, key=None, cmp=None):
    n = len(arr)
    ret = arr[:]
    if key == None:
        def key(x): return x
    if cmp == None:
        def cmp(x, y):
            return x < y
    for i in range(n-1, 0, -1):
        mx = 0
        for j in range(1, i):
            if cmp(key(ret[j]), key(ret[mx])):
                mx = j
        ret[mx], ret[i] = ret[i], ret[mx]
    return ret


