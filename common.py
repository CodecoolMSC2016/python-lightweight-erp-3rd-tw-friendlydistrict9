# implement commonly used functions here

import random
import sys
import string
import time

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def generate_random(table):
    """Create a unique id from a list
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    contain = [lower, upper, numbers, numbers, upper, lower]

    while True:
        generated = ''
        for items in range(len(contain)):
            generated += contain[items][random.randint(0, len(contain[items])-1)]
        generated += "#&"
        if generated not in table:
            return generated


def check_rows(table, title_list):
    """Checks if rows and header in a table has the same length
    """
    row_len = 0
    for row in table:
        if row_len == 0:
            for data in row:
                row_len += 1
        elif row_len == len(row):
            pass
        else:
            raise IndexError("Difference in rows' length")
    if not len(title_list) == row_len:
        raise IndexError("Title list and rows' length are different")


def get_col_lengths(tablestruct):
    """Returns a dictionary with the table column indexes which contain
        the longest word at that index from the whole table
    """
    cols = {}
    for row in tablestruct:
        for i in range(len(row)):
            try:
                if cols[i] < len(str(row[i])):
                    cols[i] += len(str(row[i]))
            except KeyError:
                cols[i] = len(str(row[i]))
    return cols


def return_col(start, blanks_char, blanks_int, content, end):
    """Returns a string which is a column's printed value in a table

    Arguments:
    start -- starting string (like: "|-")
    blanks_char -- the character you fill the blank area with(it will be multiplied)
    blanks_int -- the value of all blank area
    content -- the string or number which is shown inside the table cell
                or it can be e.g "-" if it's in the border
    end -- ending string
    """
    bl = str(blanks_char)*int(int(blanks_int)/2)
    return (str(start) + bl + content + bl + str(end))


def id_search(check_id, table, dictionary):
    ids = []
    for datas in table:
        ids.append(datas[dictionary["id"]])

    if check_id in ids:
        return True
    else:
        raise ValueError("There is no id like '" + check_id + "' :(")
        return None


def char_check(char, check, title):
    for chars in range(len(char)):
        if char[chars] in check:
            return True
    if "year" in title.lower():
        if len(char) == 4:
            return True
    elif "month" in title.lower():
        if int(char) <= 12:
            return True
    elif "day" in title.lower():
        if int(char) <= 31:
            return True
    elif "number" in title.lower():
        if char == int(char):
            return True
    else:
        raise ValueError("Please enter only the correct form :(")