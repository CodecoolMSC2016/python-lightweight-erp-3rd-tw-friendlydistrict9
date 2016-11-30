# implement commonly used functions here

import random
import sys
import ui


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


def get_col_lengths(tablestruct):
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


def open_file(filename):
    with open(filename, "r") as data:

        database = []

        for line in data:
            database.append(lines.strip().split(";"))

    return database

def navigate_sub_menus(name, options):
    while True:
        ui.print_menu(name, options, "Return to main menu")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            return option
        except KeyError as err:
            ui.print_error_message(err)