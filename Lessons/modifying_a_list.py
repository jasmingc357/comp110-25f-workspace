"""modying a list"""


def remove_first(value: int, lst: list[int]) -> None:
    """this will remove the first instance of the value in the list"""
    i: int = 0
    while i < len(lst):
        if lst[i] == value:
            lst.pop(i)
            return
        i = i + 1
    return
