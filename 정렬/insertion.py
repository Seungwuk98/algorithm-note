def insertion_sort(arr: list, key=None, cmp=None):
    ret = arr[:]
    n = len(arr)
    for i in range(1, n):
        tmp = ret[i]
        for j in range(i, 0, -1):
            if key(tmp) < key(ret[j-1]):
                ret[j] = ret[j-1]
            else :
                break
        ret[j-1] = tmp
    return ret
