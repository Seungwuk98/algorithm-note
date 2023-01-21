def fibonacci(x: int) -> int:
    if x < 2:
        return x
    return fibonacci(x-1) + fibonacci(x-2)
