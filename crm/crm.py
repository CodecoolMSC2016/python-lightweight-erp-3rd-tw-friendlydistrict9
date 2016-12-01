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

file = "crm/customers.csv"
csv_file = data_manager.get_table_from_file("crm/customers.csv")
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
            show_table(csv_file)
        elif key == "2":
            add(csv_file)
        elif key == "3":
            try:
                check_id = False
                while check_id != True:
                    remove_id = ui.get_inputs(["Please enter the id what you want to remove: "], "Remove")
                    check_id = common.id_search(remove_id[0], csv_file, names)
                    if remove_id != None:
                        remove(csv_file, remove_id[0])
            except ValueError as err:
                ui.print_error_message(err)
        elif key == "4":
            try:
                check_id = False
                while check_id != True:
                    update_id = ui.get_inputs(["Please enter the id what you want to update: "], "Update")
                    check_id = common.id_search(update_id[0], csv_file, names)
                    if update_id != None:
                        update(csv_file, update_id[0])
            except ValueError as err:
                ui.print_error_message(err)
        elif key == "5":
            get_longest_name_id(csv_file)
        elif key == "6":
            get_subscribed_emails(csv_file)
        elif key == "0":
            break
        else:
            raise KeyError("There is no such option.")

# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    titles = []
    for count in range(len(names)):
        for title in names:
            if names[title] == count:
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
    new_data = ui.get_inputs(["Name: ", "email: ", "Subscribed (Y/N): "], "Add new data")
    if new_data != None:
        while True:
            if new_data[2][0].lower() == "y":
                new_data[2] = "1"
                break
            elif new_data[2][0].lower() == "n":
                new_data[2] = "0"
                break
            elif new_data[2][0].lower() != "y" or "n":
                new_data[2] = ui.get_inputs(["Is this person subscriped? (Y/N): "], "Subscriped")
        if new_data[2] != None:
            new_game = [new_id, new_data[0], new_data[1], new_data[2]]
            table.append(new_game)
            data_manager.write_table_to_file(file, table)
            return table

# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    global csv_file

    new_list = []

    for lines in range(len(table)):
        if table[lines][names["id"]] != id_:
            new_list.append(table[lines])
    csv_file = new_list

    data_manager.write_table_to_file(file, csv_file)
    return csv_file

# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    global csv_file

    new_list = []
    update_data = ui.get_inputs(["Name: ", "email: ", "Subscribed (Y/N): "], "Update data")
    if update_data != None:
        for line in range(len(table)):
            if table[line][names["id"]] != id_:
                new_list.append(table[line])
            elif table[line][names["id"]] == id_:
                while True:
                    if update_data[2][0].lower() == "y":
                        update_data[2] = "1"
                        break
                    elif update_data[2][0].lower() == "n":
                        update_data[2] = "0"
                        break
                    elif update_data[2][0].lower() != "y" or "n":
                        update_data[2] = ui.get_inputs(["Is this person subscriped? (Y/N): "], "Subscriped")
                modified = [id_, update_data[0], update_data[1], update_data[2]]
                new_list.append(modified)
        csv_file = new_list
        data_manager.write_table_to_file(file, csv_file)
        return csv_file

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
