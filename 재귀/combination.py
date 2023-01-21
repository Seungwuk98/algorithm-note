
def combination(arr: list, select: int):
    n = len(arr)
    ret = []

    def _combination(start: int, now: list):
        if len(now) == select:
            ret.append(tuple(now))
            return
        for i in range(start, n):
            now.append(arr[i])
            _combination(i + 1, now)
            now.pop()
    _combination(0, [])
    return ret


def combination_allow_duplication(arr: list, select: int):
    n = len(arr)
    ret = []
    now = []

    def _combination_allow_duplication(start: int):
        if len(now) == select:
            ret.append(tuple(now))
            return
        for i in range(start, n):
            now.append(arr[i])
            _combination_allow_duplication(i)
            now.pop()
    _combination_allow_duplication(0)
    return ret


def permutation(arr: list, select: int):
    n = len(arr)
    ret = []
    check = [False] * n
    now = []

    def _permutation():
        if len(now) == select:
            ret.append(tuple(now))
            return
        for i in range(n):
            if not check[i]:
                check[i] = True
                now.append(arr[i])
                _permutation()
                now.pop()
                check[i] = False
    _permutation()
    return ret


if __name__ == "__main__":
    print(combination([1, 2, 3, 4], 2))
    print(combination_allow_duplication([1, 2, 3, 4], 2))
    print(permutation([1, 2, 3, 4], 2))
