import common
import os
import time

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    tablestruct = [title_list]
    for row in table:
        tablestruct.append(row)
    print(tablestruct)
    cols = common.get_col_lengths(tablestruct)
    print(cols)
    print("\n")
    for i in range(len(tablestruct)):
        for k in range(2):
            row_str = ""
            for j in range(len(tablestruct[i])):
                word = tablestruct[i][j]
                blank = (common.increase_to_even(cols[j])-len(str(word)))
                if k == 0:
                    row_str += common.return_col("|-", "-", blank, len(str(word))*"-", "-")
                elif k == 1:
                    row_str += common.return_col("| ", " ", blank, str(word), " ")
            row_str += "|"
            print(row_str)



table1 = [
    [0, "Counter strike", "fps"],
    [1, "fo", "fps"],
    [2, "anything", "console"],
    [10, "GTA V", "fdf"],
    [11, "fodsd", "fps"],
    [12, "shit", "c"]
]

titles1 = ["ID", "Title", "Type"]

#TRY OUT HERE:
print_table(table1, titles1)



# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    # your code

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")

def print_menu(title, list_options, exit_message):
    """Print the menu. Each of every menu, the console will be cleared. - David Szilagyi
    """
    os.system("clear")
    print(("\n" + title + ":"))
    for i in range(1, len(list_options) + 1):
        print("(" + str(i) + ") " + list_options[i - 1])
    print("(0) " + exit_message)

def navigate_sub_menus(name, options):
    """This will create the sub menu which is selected by
    the user in the main menu.
    name -- definied by module in the 'module_name'
    options -- definied by module in the 'options'
    inputs -- if the user input more than 1 character it will
              only get the first character
    get_inputs -- see description in the 'get inputs' def - David Szilagyi
    """
    while True:
        print_menu(name, options, "Return to main menu")
        try:
            inputs = get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            return option
        except KeyError as err:
            print_error_message(err)

# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user


def get_inputs(list_labels, title):
    """Get an input from the user. 
    Every character will be appended to a list. - David Szilagyi
    """
    inputs = []

    get_ = input(list_labels[0])
    for i in get_:
        inputs.append(i)

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message


def print_error_message(message):
    print("\033[91m" + "Error: " + str(message) + "\033[0m")
    time.sleep(2)
