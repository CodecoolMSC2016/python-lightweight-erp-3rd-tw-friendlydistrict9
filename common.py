# implement commonly used functions here

import random
import sys

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):

    generated = ''

    # your code

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



def increase_to_even(num):
    if not num % 2 == 0:
        num += 1
    return num


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



def open_file(filename):
    """Open the existing file which is contains the datas and
    add everything in a list. The each elements is separated 
    by ';' and the elements is also by it in the list - David Szilagyi
    """
    with open(filename, "r") as datas:

        database = []

        for lines in datas:
            database.append(lines.strip().split(";"))

    return database
