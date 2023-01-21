def selection_sort(arr: list, key=None, cmp=None):
    n = len(arr)
    ret = arr[:]
    for i in range(n-1, 0, -1):
        mx = 0
        for j in range(1, i+1):
            if key(ret[mx]) < key(ret[j]):
                mx = j
        ret[mx], ret[i] = ret[i], ret[mx]
    return ret


