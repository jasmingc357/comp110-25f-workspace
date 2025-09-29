"""Mutating Functions"""

__author__: str = "730620666"


def manual_append(the_list: list[int], value: int) -> None:
    """This function will mutate its input by appending the int."""
    the_list.append(value)
    return None


def double(the_list: list[int]) -> None:
    """This function will mutate its input by looping through and doubling each int"""
    i: int = 0
    while i < len(the_list):
        the_list[i] = the_list[i] * 2
        i = i + 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)

print(list_1)
print(list_2)
