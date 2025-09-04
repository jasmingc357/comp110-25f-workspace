"""practice calling + defining functions."""

from random import randint

# ptint(len("Comp110"))

# print(randint(1, 10))

"""
Write a function called sum
that takes two ints: num1 and num2 as inputs
and returns the sum of the two numbers.
"""


# Function DEFINITION
def sum(num1: int, num2: int) -> int:
    """Add two numbers."""
    return num1 + num2


# Function CALL
print(sum(num1=5, num2=7))
