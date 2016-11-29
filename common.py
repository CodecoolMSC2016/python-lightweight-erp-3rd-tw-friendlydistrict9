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
