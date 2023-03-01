"""EX04 - Utility Functions."""
__author__ = "730405020"


def all(x: list[int], a: int) -> bool:
    """States whether or not the final integer is equal to the others."""
    if len(x) == 0:
        return False
    idx: int = 0
    while idx <= len(x) - 1:
        if a == x[idx]:
            idx = idx + 1
        else:
            return False
    return True
        
    
def max(y: list[int]) -> int:
    """States the maximum value in the list."""
    if len(y) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0 
    number: int = y[idx]
    while idx <= len(y) - 1:
        if y[idx] >= number:
            number: int = y[idx]
        idx = idx + 1
    return number

        
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """States whether or not the lists are equal at every element."""
    idx: int = 0
    if len(list_1) != len(list_2):
        return False
    else:
        while idx <= len(list_1) - 1:
            if list_1[idx] == list_2[idx]:
                idx = idx + 1
            else:
                return False
        return True
            
