def merge_sort(arr: list, key=None, cmp=None):
    ret = arr[:]
    n = len(arr)
    help = [0] * n
    if key == None:
        key = lambda x : x
    if cmp == None:
        def cmp(x, y):
            return x < y
    def _merge_sort(s: int, e: int):
        if s < e:
            mid = (s + e) // 2
            _merge_sort(s, mid)
            _merge_sort(mid+1, e)
            k = 0
            i = s
            j = mid+1
            while i <= mid and j <= e:
                while i <= mid and cmp(ret[i], ret[j]):
                    help[k] = ret[i]
                    i += 1
                    k += 1
                while j <= e and not cmp(ret[i], ret[j]):
                    help[k] = ret[j]
                    j += 1
                    k += 1
            while i <= mid:
                help[k] = ret[i]
                i += 1
                k += 1
            while j <= e:
                help[k] = ret[j]
                j += 1
                k += 1
            for i in range(k):
                ret[s] = help[i]
                s += 1
    _merge_sort(0, n-1)
    return ret


