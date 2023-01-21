def bubble_sort(arr: list):
    ret = arr[:]
    n = len(ret)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ret[j+1] < ret[j]:
                ret[j], ret[j+1] = ret[j+1], ret[j]
    return ret
