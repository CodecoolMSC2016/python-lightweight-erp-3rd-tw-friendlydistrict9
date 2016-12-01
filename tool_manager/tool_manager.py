# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

table = data_manager.get_table_from_file("tool_manager/tools.csv")
names = {"id": 0, "name": 1, "manufacturer": 2, "purchase_date": 3, "durability": 4}

def start_module():
    while True:
        module_name = "Tool manager"

        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "Available tools",
                   "Average durability by manufacturers"]

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
            get_available_tools(table)
        elif key == "6":
            get_average_durability_by_manufacturers(table)
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
    title = ui.get_inputs(["Please enter the name of the tool: "], "Name")
    man = ui.get_inputs(["Please enter the manufacturer of the tool: "], "Manufacturer")
    date = ui.get_inputs(["Please enter when you bought the tool: "], "Purchased date")
    durability = ui.get_inputs(["Please enter the durability of the tool: "], "Durability")

    new_game = [new_id, title[0], man[0], date[0], durability[0]]

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

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
