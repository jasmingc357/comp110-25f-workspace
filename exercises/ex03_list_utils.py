"""Excersise 3 - List Utils."""

__author__: str = "730620666"


def all(the_list: list[int], number: int) -> bool:
    """the bool will tell if the items in the list are the same as the number given"""
    i: int = 0  # this will start at the beggining of the list
    if (
        len(the_list) == 0
    ):  # this is for an empty list , otherwise follow the while loop
        return False
    while i < len(the_list):  # i will go through the list
        if (
            the_list[i] != number
        ):  # if that item # dont match the number given, then it return false
            return False
        i = i + 1  # after returning false, it will keep going through the list
    return True


print(all([1, 2, 1], 1))


def max(the_list: list[int]) -> int:
    """This function will return the largest number of the list."""
    if len(the_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    largest: int = the_list[0]
    while i < len(the_list):
        if the_list[i] > largest:
            largest = the_list[i]  # this becomes the new largest int
        i = i + 1  # this is the then statement, after largest is evaluated
    return largest


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """This function will return True if the two lists are the same"""
    if (
        list_1 != list_2
    ):  # this checks if every element at every index is equal to both lists
        return False
    i: int = 0
    while i < len(list_1):  # this while loop will go through the list
        if list_1[i] != list_2[i]:  # if the items at the same index are different
            return False  # then its false
        i = i + 1  # this is after the if statement is evaluated
    return True  # if it goes through the whole list
    # and finds no differences, they are equal


def extend(list_1: list[int], list_2: list[int]) -> None:
    """This function will mutate second list to the first, using appending."""
    i: int = 0
    while i < len(list_2):
        list_1.append(list_2[i])
        i = i + 1
        new_list = list_1
    return None


a: list[int] = [1, 2, 3]
b: list[int] = [4, 6, 6]
extend(a, b)
