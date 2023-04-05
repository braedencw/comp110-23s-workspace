"""EX07 - Dictionary Functions."""
__author__ = "730405020"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts initial dictionary."""
    inverted: dict[str, str] = {}
    for key in dictionary:
        value = dictionary[key]
        if value in inverted:
            raise KeyError("KeyError")
        else:
            inverted[value] = key
    return inverted
    

def favorite_color(dictionary: dict[str, str]) -> str:
    """Determines and returns favorite color from dictionary."""
    new_dict: dict[str, int] = {}
    for person in dictionary:
        color = dictionary[person]
        if color in new_dict:
            new_dict[color] += 1
        else: 
            new_dict[color] = 1
    max_color: int = 0
    return_color: str = ""
    for color in new_dict:
        if new_dict[color] > max_color:
            max_color = new_dict[color]
            return_color = color
    return return_color


def count(list: list[str]) -> dict[str, int]:
    """Returns a dictionary showing how many times an item was in a list."""
    dictionary: dict[str, int] = {}
    for item in list:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary 