"""EX05 - list Utility Functions."""
__author__ = "730405020"

def only_evens(numbers: list[int]) -> list[int]:
    """returns list of even integers/numbers from input parameters."""
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens

def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """returns a list containing all elements of 1st and 2nd lists."""
    final_list = []
    for n in list_1:
        final_list.append(n)
    for n in list_2:
        final_list.append(n)
    return final_list

def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """returns a subset of a given list between specified start and end indexes."""
    if start_idx < 0:
        start_idx = 0 
    if end_idx > len(a_list):
        end_idx = len(a_list) - 1
    sub_list = a_list[start_idx: end_idx]
    return sub_list
