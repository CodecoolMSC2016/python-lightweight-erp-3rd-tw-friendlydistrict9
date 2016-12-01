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
data_manager = SourceFileLoader(
    "data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#

file = "accounting/items.csv"
csv_file = data_manager.get_table_from_file("accounting/items.csv")
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
            show_table(csv_file)
        elif key == "2":
            add(csv_file)
        elif key == "3":
            try:
                check_id = False
                while check_id != True:
                    remove_id = ui.get_inputs(
                        ["Please enter the id what you want to remove: "], "Remove")
                    check_id = common.id_search(remove_id[0], csv_file, names)
                    if remove_id != None:
                        remove(csv_file, remove_id[0])
            except line_amountError as err:
                ui.print_error_message(err)
        elif key == "4":
            try:
                check_id = False
                while check_id != True:
                    update_id = ui.get_inputs(
                        ["Please enter the id what you want to update: "], "Update")
                    check_id = common.id_search(update_id[0], csv_file, names)
                    if update_id != None:
                        update(csv_file, update_id[0])
            except line_amountError as err:
                ui.print_error_message(err)
        elif key == "5":
            which_year_max(csv_file)
        elif key == "6":
            year = ui.get_inputs(
                ["Enter a year:"], "Input year")
            avg_amount(csv_file, year)
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

    new_data = ui.get_inputs(["Month: ", "Day: ", "Year: ",
                              "Income or Outcome (in/out): ", "Amount: "], "Add new data")
    if new_data != None:
        while True:
            if new_data[3][0].lower() == "in":
                new_data[3] = "in"
                break
            elif new_data[3][0].lower() == "out":
                new_data[3] = "out"
                break
            elif new_data[3][0].lower() != "in" or "out":
                new_data[3] = ui.get_inputs(
                    ["Is it income (in) or outcome (out): "], "In or Out")
        new_game = [new_id, new_data[0], new_data[1],
                    new_data[2], new_data[3], new_data[4]]
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

    update_data = ui.get_inputs(
        ["Month: ", "Day: ", "Year: ", "Income or Outcome (in/out): ", "Amount: "], "Update data")
    if update_data != None:
        for line in range(len(table)):
            if table[line][names["id"]] != id_:
                new_list.append(table[line])
            elif table[line][names["id"]] == id_:
                while True:
                    if update_data[3][0].lower() == "in":
                        update_data[3] = "in"
                        break
                    elif update_data[3][0].lower() == "out":
                        update_data[3] = "out"
                        break
                    elif update_data[3][0].lower() != "in" or "out":
                        update_data[3] = ui.get_inputs(
                            ["Is it income (in) or outcome (out): "], "In or Out")
                modified = [id_, update_data[0], update_data[1],
                            update_data[2], update_data[3], update_data[4]]
                new_list.append(modified)
        csv_file = new_list
        data_manager.write_table_to_file(file, csv_file)
        return csv_file


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)


def which_year_max(table):
    year_dictionary = {}
    max_profit = 0
    max_year = 0
    for line in table:
        try:
            if line[names["type"]] == "in":
                year_dictionary[line[names["year"]]
                                ] += int(line[names["amount"]])
            else:
                year_dictionary[line[names["year"]]
                                ] -= int(line[names["amount"]])
        except KeyError:
            if line[names["type"]] == "in":
                year_dictionary[line[names["year"]]] = int(
                    line[names["amount"]])
            else:
                year_dictionary[line[names["year"]]] = - \
                    int(line[names["amount"]])

    for year, profit in year_dictionary.items():
        if profit > max_profit:
            max_profit = profit
            max_year = year

    ui.print_result(str(max_year), "This year has the highest profit:")
    return int(max_year)


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    profit = 0
    item_counter = 0
    given_year = int(year[0])
    for line in table:
        line_type = line[names["type"]]
        line_amount = int(line[names["amount"]])
        line_year = int(line[names["year"]])
        if line_year == given_year:
            if line_type == "out":
                profit -= line_amount
            else:
                profit += line_amount
            item_counter += 1
    average = profit / item_counter
    ui.print_result(average, "The average profit:")
    return average
