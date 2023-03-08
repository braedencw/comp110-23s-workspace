"""EX05 - list Utility Functions."""
__author__ = "730405020"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty() -> None:
    """Edge case: will function give an empty list if input is all odd?"""
    test_list: list[int] = [3, 5, 7]
    assert only_evens(test_list) == []


def test_evens_1() -> None:
    """Use case: will function pick even numbers out of list?"""
    test_list: list[int] = [1, 4, 7]
    assert only_evens(test_list) == [4]


def test_evens_2() -> None:
    """Use case: will function pick even numbers out of list?"""
    test_list: list[int] = [2, 3, 6]
    assert only_evens(test_list) == [2, 6]


def test_empty_2() -> None:
    """Edge case: will function add empty list to filled list?"""
    test_list_1: list[int] = [3, 5, 7]
    test_list_2: list[int] = []
    assert concat(test_list_1, test_list_2) == [3, 5, 7]


def test_add_1() -> None:
    """Use case: will function combine both lists together?"""
    test_list_1: list[int] = [3, 5, 7]
    test_list_2: list[int] = [2, 3, 6]
    assert concat(test_list_1, test_list_2) == [3, 5, 7, 2, 3, 6]


def test_add_2() -> None:
    """Use case: will function combine both lists together?"""
    test_list_1: list[int] = [1, 5, 7]
    test_list_2: list[int] = [2, 6, 8]
    assert concat(test_list_1, test_list_2) == [1, 5, 7, 2, 6, 8]


def test_negative() -> None:
    """Edge case: will the function start from the beginnig of the list if start index is negative?"""
    a_list: list[int] = [1, 2, 3, 4]
    start_idx = -1
    end_idx = 3
    assert sub(a_list, start_idx, end_idx) == [1, 2, 3]


def test_positive_1() -> None:
    """Use case: will the function make the subset in the proper range?"""
    a_list: list[int] = [1, 2, 3, 4]
    start_idx = 1
    end_idx = 3
    assert sub(a_list, start_idx, end_idx) == [2, 3]
    

def test_positive_2() -> None:
    """Use case: will the function make the subset in the proper range?"""
    a_list: list[int] = [1, 2, 3, 4]
    start_idx = 2
    end_idx = 4
    assert sub(a_list, start_idx, end_idx) == [3, 4]
