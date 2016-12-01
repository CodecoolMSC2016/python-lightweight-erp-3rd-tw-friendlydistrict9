# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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

file = "hr/persons.csv"
csv_file = data_manager.get_table_from_file("hr/persons.csv")
names = {"id": 0, "name": 1, "birth_date": 2}

def start_module():
    while True:
        module_name = "Human resources manager"

        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "Show oldest person",
                   "Persons closest to average"]

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
            except ValueError as err:
                ui.print_error_message(err)
            remove(csv_file, remove_id[0])
        elif key == "4":
            try:
                check_id = False
                while check_id != True:
                    update_id = ui.get_inputs(["Please enter the id what you want to update: "], "Update")
                    check_id = common.id_search(update_id[0], csv_file, names)
            except ValueError as err:
                ui.print_error_message(err)
            update(csv_file, update_id[0])
        elif key == "5":
            get_oldest_person(csv_file)
        elif key == "6":
            get_persons_closest_to_average(csv_file)
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
    new_data = ui.get_inputs(["Name: ", "Birth date: "], "Add new data")
    if new_data != None:
        new_game = [new_id, new_data[0], new_data[1]]
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
    update_data = ui.get_inputs(["Name: ", "Birth date: "], "Update data")
    if update_data != None:
        for line in range(len(table)):
            if table[line][names["id"]] != id_:
                new_list.append(table[line])
            elif table[line][names["id"]] == id_:
                modified = [id_, update_data[0], update_data[1]]
                new_list.append(modified)
        csv_file = new_list
        data_manager.write_table_to_file(file, csv_file)
        return csv_file

# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
