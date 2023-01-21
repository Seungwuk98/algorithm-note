def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    left = [item for item in arr if item < pivot]
    right = [item for item in arr if pivot <= item]

    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_three_part(arr: list):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [item for item in arr if item < pivot]
    same = [item for item in arr if item == pivot]
    right = [item for item in arr if pivot < item]

    return quick_sort(left) + same + quick_sort(right)


