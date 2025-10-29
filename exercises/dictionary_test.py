"""this will test exercise 4"""

__author__ = "730620666"

import pytest
from exercises.ex04.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


def test_invert() -> None:
    """this will test the invert function"""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert2() -> None:
    """this will test the invert function"""
    assert invert({"hello": "hi", "goodbye": "bye"}) == {
        "hi": "hello",
        "bye": "goodbye",
    }
 

def test_invert3() -> None:
    """this will test the invert function on an empty dict"""
    assert invert({}) == {}
    # what happends when there is an empty dictionary


# this function is reversing the spots of key with values


with pytest.raises(KeyError):
    my_dictionary = {"alyssa": "byrnes", "adam": "byrnes"}
    invert(my_dictionary)
# this is used to test if the keyerror is being raised when there is a duplicate


def test_favorite_color() -> None:
    """this will test the favorite color function"""
    assert favorite_color({"Marc": "yellow", "Ezri": "pink", "Kris": "pink"}) == "pink"
    # essentially the common color is yellow .. should return "pink"


def test_favorite_color2() -> None:
    """this will test the favorite color function"""
    assert (
        favorite_color({"Marc": "yellow", "Ezri": "yellow", "Kris": "emerald"})
        == "yellow"
    )  # essentially the common color is yellow .. should return "yellow"


def test_favorite_color3() -> None:
    """this will test the favorite color function"""
    assert favorite_color({"Marc": "green", "Ezri": "blue", "Kris": "red"}) == "green"


# this last assert is testing when everything is tie,
#  it should return the first popular color


def test_count() -> None:
    """this will test the count function in using a list into a dict"""
    assert count(["apple", "banana", "apple", "orange", "banana", "apple"]) == {
        "apple": 3,
        "banana": 2,
        "orange": 1,
    }  # from here we are testing to see if it counted all 3 apples


def test_count2() -> None:
    """this will test the count function in using a list into a dict"""
    assert count(["cat", "dog", "cat", "cat", "dog", "fish"]) == {
        "cat": 3,
        "dog": 2,
        "fish": 1,
    }  # this one is counting as well


def test_count3() -> None:
    """this will test the count function in using a list into a dict"""
    assert count([]) == {}
    # this one is counting an empty list, technically should be zero


def test_alphabetizer() -> None:
    """this is going to make a dictionary with keys
    being the first letter of each word and the words will follow a the values"""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {
        "c": ["cat", "car"],
        "a": ["apple", "angry"],
        "b": ["boy", "bad"],
    }


def test_alphabetizer2() -> None:
    """this is going to make a dictionary with keys
    being the first letter of each word and the words will follow a the values"""
    list_name = {"one", "two", "three", "four"}
    assert alphabetizer(list_name) == {
        "o": ["one"],
        "t": ["two", "three"],
        "f": ["four"],
    }


def test_alphabetizer3() -> None:
    """this is going to make a dictionary with keys
    being the first letter of each word and the words will follow a the values"""
    assert alphabetizer([]) == {}
    # the last one should test an empty list


def test_update_attendance() -> None:
    """this test will take in 1 dict, and 2 string parameters , this will
    update the dict by adding students to monday"""
    existing_log = {"Monday": ["Virinda"]}
    update_attendance(existing_log, "Monday", "Kaleb")
    assert existing_log == {"Monday": ["Virinda", "Kaleb"]}


def test_update_attendance2() -> None:
    """this test will take in 1 dict, and 2 string parameters , this will
    update the dict by adding students to another day"""
    existing_log = {"Monday": ["Virinda"]}
    update_attendance(existing_log, "tuesday", "Kaleb")
    assert existing_log == {"Monday": ["Virinda"], "tuesday": ["Kaleb"]}


def test_update_attendance3() -> None:
    """this test will make sure not to add the same student to the same day"""
    # this will reduce duplicate incidents
    existing_log = {"Monday": ["Virinda"]}
    update_attendance(existing_log, "Monday", "Virinda")
    assert existing_log == {"Monday": ["Virinda"]}
