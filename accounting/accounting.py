# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#

table = data_manager.get_table_from_file("accounting/items.csv")
names = {"id": 0, "month": 1, "day": 2, "year": 3, "type": 4, "amount": 5}

def start_module():
    while True:
        module_name = "Accounting manager"

        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "Maximum profit",
                   "Average profit"]

        key = ui.navigate_sub_menus(module_name, options)

        if key == "1":
            show_table(table)
        elif key == "2":
            add(table)
        elif key == "3":
            remove(table, id_)
        elif key == "4":
            update(table, id_)
        elif key == "5":
            which_year_max(table)
        elif key == "6":
            avg_amount(table, year)
        elif key == "0":
            break
        else:
            raise KeyError("There is no such option.")

# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    titles = []

    for title in names:
        titles.append(title)

    ui.print_table(table, titles)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    
    ids = []
    for datas in table:
        ids.append(datas[names["id"]])
    new_id = common.generate_random(ids)
    month = ui.get_inputs(["Please enter the month: "], "Month")
    day = ui.get_inputs(["Please enter the day: "], "Day")
    year = ui.get_inputs(["Please enter the year: "], "Year")
    while True:
        in_or_out = ui.get_inputs(["Is it income (in) or outcome (out): "], "In or Out")
        if in_or_out[0].lower() == "in":
            in_or_out = "in"
        elif in_or_out[0].lower() == "out":
            in_or_out = "out"
    amount = ui.get_inputs(["Please enter the amount: "], "Amount")

    new_game = [new_id, month[0], day[0], year[0], in_or_out, amount[0]]

    table.append(new_game)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
