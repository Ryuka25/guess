from random import randint


def addition(a: int, b: int) -> int:
    """
    Use: Detects if numbers are in extreme ranges

    - If result is random (180-199), you know a + b >= 180 → both numbers are large
    - If result is random (3-20), you know a + b <= 20 → both numbers are small
    - If result equals exact sum, you know 20 < a + b < 180 → moderate range
    """
    r = a + b
    if r >= 180:
        return randint(180, 199)
    if r <= 20:
        return randint(3, 20)
    return r


def multiplication(a: int, b: int) -> int:
    """
    Use: Reveals the last digit pattern
    """
    r = a * b
    return r % 10


def division(a: int, b: int) -> int:
    """
    Use: Determines relative size and divisibility

    - Always returns the larger divided by the smaller
    - Result tells you the "order of magnitude" difference
    """
    if a > b:
        return a // b
    return b // a


def zero(a: int, b: int) -> int:
    """
    Use: Reveals tens-digit proximity and detects multiples of 10
    """
    r = abs((a // 10) - (b // 10))
    if a % 10 == 0:
        return r + 1
    return r
