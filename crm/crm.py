# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

table = data_manager.get_table_from_file("crm/customers.csv")
names = {"id": 0, "name": 1, "email": 2, "subscribed": 3}

def start_module():
    while True:
        module_name = "Customer Relationship Management (CRM)"

        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "Longest name",
                   "Subscribed emails"]

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
            get_longest_name_id(table)
        elif key == "6":
            get_subscribed_emails(table)
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
    name = ui.get_inputs(["Please enter the person's name: "], "Name")
    email = ui.get_inputs(["Please enter the email: "], "Email")
    subscriped = ui.get_inputs(["Is this person subscriped? Y/N: "], "Subscriped")
    while True:
        if subscriped[0].lower() == "y":
            subscriped = "1"
            break
        elif subscriped[0].lower() == "n":
            subscriped = "0"
            break
        elif subscriped[0].lower != "y" or "n":
            subscriped = ui.get_inputs(["Is this person subscriped? Y/N: "], "Subscriped")

    new_game = [new_id, name[0], email[0], subscriped]

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


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
