"""Practicing recusion."""


def f(n: int, b: int) -> int:
    """using BC and RR"""
    if n == 0:
        return b
    else:
        return f(n - 1, b) + 1


# print(f(3, 4))


# practice code writing !


def sum(number: int) -> int:
    """sums up all non-negative integers up to an including ..."""
    if number < 0:  # (base case)
        return -1
    elif number > 0:  # (recusive)
        return number + sum(number=number - 1)
    else:  # base case
        return 0


print(sum(number=4))
