# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader(
    "data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common", current_file_path + "/../common.py").load_module()

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#

file = "store/games.csv"
csv_file = data_manager.get_table_from_file("store/games.csv")
names = {"id": 0, "title": 1, "manufacturer": 2, "price": 3, "in stock": 4}


def start_module():
    while True:
        module_name = "Store manager"

        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "Counts by manufacturers",
                   "Average by manufacturer"]

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
            get_counts_by_manufacturers(csv_file)
        elif key == "6":
            manufacturer = ui.get_inputs(
                ["Enter a manufacturer:"], "Input manufacturer")
            manufacturer = str(manufacturer[0])
            get_average_by_manufacturer(csv_file, manufacturer)
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
    new_data = ui.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "In stock: "], "Add new data")
    if new_data != None:
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

    for line in range(len(table)):
        if table[line][names["id"]] != id_:
            new_list.append(table[line])
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

    update_data = ui.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "In stock: "], "Update data")
    if update_data != None:
        for line in range(len(table)):
            if table[line][names["id"]] != id_:
                new_list.append(table[line])
            elif table[line][names["id"]] == id_:
                modified = [id_, update_data[0], update_data[1], update_data[2], update_data[3]]
                new_list.append(modified)
        csv_file = new_list
        data_manager.write_table_to_file(file, csv_file)
        return csv_file

# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturer_dictionary = {}
    for line in table:
        try:
            manufacturer_dictionary[line[names["manufacturer"]]] += 1
        except KeyError:
            manufacturer_dictionary[line[names["manufacturer"]]] = 1
    ui.print_result(manufacturer_dictionary, "Different kinds of game are available:")
    return manufacturer_dictionary


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    game_counter = 0
    amount = 0
    for line in table:
        if line[names["manufacturer"]] == manufacturer:
            game_counter += 1
            amount += int(line[names["in stock"]])
    average = amount / game_counter
    ui.print_result(average, "The average amount:")
    return average
