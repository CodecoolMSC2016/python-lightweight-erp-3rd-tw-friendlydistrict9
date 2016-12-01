# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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

file = "selling/sellings.csv"
csv_file = data_manager.get_table_from_file("selling/sellings.csv")
names = {"id": 0, "title": 1, "price": 2, "month": 3, "day": 4, "year": 5}


def start_module():
    while True:
        module_name = "Selling manager"

        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "Lowest price",
                   "Sold between 2 dates"]

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
            get_lowest_price_item_id(csv_file)
        elif key == "6":
            ui.get_inputs()
            month_from = dates[0]
            day_from = dates[1]
            year_from = dates[2]
            month_to = dates[3]
            day_to = dates[4]
            year_to = dates[5]
            get_items_sold_between(
                table, month_from, day_from, year_from, month_to, day_to, year_to)
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
    new_data = ui.get_inputs(["Title: ", "Price: ", "Month: ", "Day: ", "Year: "], "Add new data")
    new_game = [new_id, new_data[0], new_data[1], new_data[2], new_data[3], new_data[4]]

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
            update_data = ui.get_inputs(["Title: ", "Price: ", "Month: ", "Day: ", "Year: "], "Update data")
            modified = [id_, update_data[0], update_data[1], update_data[2], update_data[3], update_data[4]]
            new_list.append(modified)
    csv_file = new_list
    data_manager.write_table_to_file(file, csv_file)
    return csv_file

# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of
# descending alphabetical order
def get_lowest_price_item_id(table):
    table = sorted(table, key=lambda x: x[
        names["title"]], reverse=True)
    table = sorted(table, key=lambda x: int(
        x[names["price"]]), reverse=False)
    # Test:
    # print(table)
    # print(table[0][names["ID"]])
    return table[0][names["id"]]


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    # Test:
    print(table)

    filtered_list = []
    date_from = year_from + month_from.zfill(2) + day_from.zfill(2)
    date_to = year_to + month_to.zfill(2) + day_to.zfill(2)
    print(date_from, date_to)
    for i in range(len(table)):
        if int(date_from) < int(table[i][names["year"]] + table[i][names["month"]].zfill(2) + table[i][names["day"]].zfill(2)) < int(date_to):
            filtered_list.append(table[i])

    print(filtered_list)
    return filtered_list
