from random import randint


def quick_sort(arr: list):
    ret = arr[:]

    def _quick_sort(s: int, e: int):
        if s < e:
            p = randint(s, e)
            pivot = ret[p]
            ret[p], ret[s] = ret[s], ret[p]
            i = s+1
            for j in range(s+1, e+1):
                if ret[j] < pivot:
                    ret[i], ret[j] = ret[j], ret[i]
                    i += 1
            i -= 1
            ret[i], ret[s] = ret[s], ret[i]
            _quick_sort(s, i-1)
            while i <= e and ret[i] == pivot:
                i += 1
            _quick_sort(i, e)
    _quick_sort(0, len(ret)-1)
    return ret
