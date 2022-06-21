def factorial_interactive(n):
    result = 1
    for i in range(1, n+1):
        result *= n
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
