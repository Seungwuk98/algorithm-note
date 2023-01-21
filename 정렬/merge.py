def merge_sort(arr: list):
    ret = arr[:]
    n = len(arr)
    help = [0] * n

    def _merge_sort(s: int, e: int):
        if s < e:
            mid = (s + e) // 2
            _merge_sort(s, mid)
            _merge_sort(mid+1, e)
            k = 0
            i = s
            j = mid+1
            while i <= mid and j <= e:
                while i <= mid and ret[i] < ret[j]:
                    help[k] = ret[i]
                    i += 1
                    k += 1
                while j <= e and ret[i] >= ret[j]:
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


