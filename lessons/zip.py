"""CQ4 - Dict Function Writing."""
__author__ = "730405020"

def zip(keys: list[str], values: list[int]):
    if keys == list() and values == list():
        return dict()
    idx: int = 0
    if len(keys) == len(values):
        dictionary = {keys[idx]: values[idx] for idx in range(len(keys))}
        return dictionary
    else:
        return dict()