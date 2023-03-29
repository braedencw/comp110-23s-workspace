"""EX07 - Unit Tests for Dictionary Functions."""
__author__ = "730405020"


from dictionary import invert, favorite_color, count
import pytest


def test_error() -> None:
    """Edge case: will function return 'KeyError' if there are two same values in dictionary?"""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(test_dict)


def test_invert_1() -> None:
    """Use case: will fucntion invert dictionary of letters?"""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2() -> None:
    """Use case: will fucntion invert dictionary?"""
    test_dict: dict[str, str] = {'apple': 'cat'}
    assert invert(test_dict) == {'cat': 'apple'}


def test_tie() -> None:
    """Edge case: will function return the color that appearred first in the dictionary?"""
    test_dict: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue', 'Braeden': 'yellow'}
    assert favorite_color(test_dict) == "yellow"


def test_favorite_color_1() -> None:
    """Use case: will function return the color that appears most in dictionary?"""
    test_dict: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_2() -> None:
    """Use case: will function return the color that appears most in dictionary?"""
    test_dict: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'yellow', 'Kris': 'blue'}
    assert favorite_color(test_dict) == "yellow"


def test_empty() -> None:
    """Edge case: will the function return an empty dictionary if list is empty?"""
    test_list: list[str] = ()
    assert count(test_list) == {}


def test_count_1() -> None:
    """Use case: will the function return an dictionary showing how many times an item was in the list?"""
    test_list: list[str] = ('yellow', 'yellow', 'blue')
    assert count(test_list) == {'yellow': 2, 'blue': 1}


def test_count_2() -> None:
    """Use case: will the function return an dictionary showing how many times an item was in the list?"""
    test_list: list[str] = ('yellow', 'yellow', 'blue', 'blue')
    assert count(test_list) == {'yellow': 2, 'blue': 2}