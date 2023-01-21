def factorial(x: int) -> int:
    if x < 2:
        return 1
    return x * factorial(x-1)
