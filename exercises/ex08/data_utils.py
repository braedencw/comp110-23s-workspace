"""EX08 - Data Wrangling."""
__author__ = "730405020"


from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: list[str]) -> list[str]:
    """Returns values in a table under a special header."""
    result: list[str] = []
    # step through table
    for row in table:
        # save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats our data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result 


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Examine just the first few rows of a table."""
    result: dict[str, list[str]] = {}
    for key in table:
        list_1: list[str] = []
        for item in range(0, N):
            if item < len(table[key]):
                list_1.append(table[key][item])
        result[key] = list_1
    return result


def select(table: dict[str, list[str]], header: list[str]) -> dict[str, list[str]]:
    """Select specific columns."""
    result: dict[str, list[str]] = {}
    for item in header:
        result[item] = table[item]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with 2 column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in table_1:
        result[key] = table_1[key]
    for key in table_2:
        if key in result:
            result[key] += table_2[key]
        else:
            result[key] = table_2[key]
    return result


def count(list: list[str]) -> dict[str, int]:
    """Count number of times a key appears in a list."""
    result: dict[str, int] = {}
    for item in list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result