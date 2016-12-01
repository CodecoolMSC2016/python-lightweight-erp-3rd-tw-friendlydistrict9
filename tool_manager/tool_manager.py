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

file = "tool_manager/tools.csv"
csv_file = data_manager.get_table_from_file("tool_manager/tools.csv")
names = {"id": 0, "name": 1, "manufacturers": 2, "purchase_date": 3, "durability": 4}


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
            show_table(csv_file)
        elif key == "2":
            add(csv_file)
        elif key == "3":
            remove_id = ui.get_inputs(["Please enter the id what you want to remove: "], "Remove")
            remove(csv_file, remove_id[0])
        elif key == "4":
            update_id = ui.get_inputs(["Please enter the id what you want to update: "], "Update")
            update(csv_file, update_id[0])
        elif key == "5":
            get_available_tools(csv_file)
        elif key == "6":
            get_average_durability_by_manufacturers(csv_file)
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
    new_data = ui.get_inputs(["Title: ", "Manufacturer: ", "Bought date: ", "Durability: "], "Add new data")
    new_game = [new_id, new_data[0], new_data[1], new_data[2], new_data[3]]
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

    for line in range(len(table)):
        if table[line][names["id"]] != id_:
            new_list.append(table[line])
        elif table[line][names["id"]] == id_:
            update_data = ui.get_inputs(["Title: ", "Manufacturer: ", "Bought date: ", "Durability: "], "Update data")
            modified = [id_, update_data[0], update_data[1], update_data[2], update_data[3]]
            new_list.append(modified)
    csv_file = new_list
    data_manager.write_table_to_file(file, csv_file)
    return csv_file

# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists


def get_available_tools(table):
    final_list = []
    curr_year = 2016

    for line in range(len(table)):
        if curr_year - int(table[line][names["purchase_date"]]) < int(table[line][names["durability"]]):
            tool = [table[line][names["id"]], table[line][names["name"]],
                    table[line][names["manufacturers"]], int(table[line][names["purchase_date"]]),
                    int(table[line][names["durability"]])]
            final_list.append(tool)

    final = ui.print_result(final_list, "Items what are not exceeded their durability yet: ")

    return final_list

# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists


def get_average_durability_by_manufacturers(table):
    avg_durability = {}
    for data in table:
        total = 0
        count = 0
        if not data[names["manufacturers"]] in avg_durability:
            for line in range(len(table)):
                if data[names["manufacturers"]] == table[line][names["manufacturers"]]:
                    total += int(table[line][names["durability"]])
                    count += 1
            avg_durability[data[names["manufacturers"]]] = float(total / count)

    result = ui.print_result(avg_durability, "Average durability time: ")

    return avg_durability
