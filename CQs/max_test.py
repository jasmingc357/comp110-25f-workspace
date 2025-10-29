"""This file will use a unit test to test the max function."""

_author__: str = "730620666"

from CQs.cq03.find_max import find_and_remove_max
 

def test_max_find_max() -> None:
    assert find_and_remove_max(b)


# returns expected value

b: list[int] = [10, 9, 8, 7, 10]


def test_max_find_with_empty_list() -> None:
    assert find_and_remove_max([]) == -1


# returns the correct value in case of an uncoventional input


def test_providing_new_list_with_max_removed() -> None:
    c: list[int] = [9, 9, 8, 7]
    assert find_and_remove_max(c) == 9


# mutaties the input in the expected way
