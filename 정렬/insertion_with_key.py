def insertion_sort(arr: list, key=None, cmp=None):
    ret = arr[:]
    n = len(arr)
    if key == None:
        key = lambda x : x
    if cmp == None:
        def cmp(x, y):
            return x < y
    for i in range(1, n):
        tmp = ret[i]
        for j in range(i, 0, -1):
            if cmp(key(ret[j-1]), key(tmp)):
                ret[j] = ret[j-1]
            else:
                break
        ret[j-1] = tmp
    return ret

a = [1234,22,7,2,3,4,72,2,7,2,5,2,42,4]

print(insertion_sort(a))