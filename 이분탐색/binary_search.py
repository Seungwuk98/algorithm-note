def lower_bound(arr: list, item: any, key=None):
    lo, hi = 0, len(arr)
    if key == None:
        key = lambda x : x
    while lo < hi:
        mid = (lo + hi) // 2
        if key(arr[mid]) < item:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr: list, item: any, key=None):
    lo, hi = 0, len(arr)
    if key == None:
        def key(x): return x
    while lo < hi:
        mid = (lo + hi) // 2
        if key(arr[mid]) <= item:
            lo = mid + 1
        else:
            hi = mid
    return lo
