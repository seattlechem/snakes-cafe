
import csv
import uuid

menus = {'Appetizers': {('Wings', 2.00): 0, ('Cookies', 15.00): 0,
         ('Spring Rolls', 4.00): 0, ('Rings', 4.00): 0,
         ('Shrimp bites', 4.00): 0, ('Wontons', 4.00): 0,
         ('Crab Dip', 4.00): 0, ('Sliders', 4.00): 0,
         ('Clams', 8.00): 0},
         'Entrees': {('Salmon', 5.00): 0, ('Steak', 6.00): 0,
                     ('Meat Tornado', 4.00): 0, ('A Literal Garden', 3.00): 0,
                     ('Pasta', 4.00): 0, ('Ribs', 4.00): 0,
                     ('Cabbage Rolls', 8.00): 0, ('Pizza', 4.00): 0,
                     ('Paella', 4.00): 0},
         'Desserts': {('Ice Cream', 500.0): 0, ('Cake', 30.00): 0,
                      ('Pie', 3.00): 0, ('Pudding', 4.00): 0,
                      ('Fruit', 4.00): 0, ('Sorbet', 4.00): 0,
                      ('Torte', 4.00): 0, ('Flan', 4.00): 0,
                      ('Apple', 4.00): 0},
         'Drinks': {('Coffee', 4.00): 0, ('Tea', 3.00): 0,
                    ('Blood of the Innocent', 6.00): 0, ('Pop', 4.00): 0,
                    ('Wine', 4.00): 0, ('Beer', 4.00): 0,
                    ('Sake', 4.00): 0, ('Cocoa', 4.00): 0,
                    ('Evian', 4.00): 0},
         'Sides': {('Frys', 4.00): 0, ('Salad', 3.00): 0,
                   ('Bread', 6.00): 0, ('Slaw', 4.00): 0, ('Soup', 4.00): 0,
                   ('Rice', 4.00): 0, ('Spinach', 4.00): 0,
                   ('Sauce', 4.00): 0, ('Crab dip', 4.00): 0}}


def menu_welcome():
    """
    Prints our welcome message
    """
    welcome = """
            ****************************************
            **     Welcome to the Snakes Cafe!    **
            **  ********************************  **
            **   To quit at any time, Type 'quit' **
            ****************************************
           """
    print(welcome)
    return welcome


def menu_items():
    """Print out the menu items."""
    menu_string = ''
    item_group = ''
    for key, value in menus.items():
        category_string = key
        for tuple_item in value:
            price = '{0:.2f}'.format(tuple_item[1])
            item_string = '{:<5}, {:>20}'.format(tuple_item[0],
                                                 '$' + str(price) + '\n')
            item_group += item_string
        menu_string += '\n' + category_string + ('-' * 10) + '\n' + item_group
        item_group = ''
    print(menu_string)
    return menu_string


def ordering():
    """
    Ask user for order.  Responds based on the user input.
    if user input is quit - program quits
    if user input is order - prints out order receipt which includes
        subtotal, tax and total
    if user input is remove - removes one of item user removes
    if user input is menu - prints menu
    if user input is a category form the menu - prints items
        in that category.

    """
    condition = True
    print(('*' * 40) + '\n' + ('*' * 2) +
          'What would you like to order?  ' + ('*' * 2) + '\n' +
          ('*' * 40) + '\n' + 'Enter quit any time to exit')
    while condition:
            order = input('>' + '\t')
            order = order.title()
            if order.split(' ')[0] == 'Quit':
                condition = False
                break
            elif order.split(' ')[0] == 'Order':
                print_receipt()
            elif order.split(' ')[0] == 'Remove':
                for value in menus.values():
                    for tuple_item in value.keys():
                        if order.split(' ')[1] == tuple_item[0]:
                            value[tuple_item] -= 1
                print_receipt()
            elif order.split(' ')[0] == 'Menu':
                menu_items()
            elif order.split(' ')[0] in menus.keys():
                for key, value in menus.items():
                    if order.split(' ')[0] == key:
                        for key in value.keys():
                            print(key[0])
            else:
                for value in menus.values():
                    for tuple_item in value.keys():
                        if order == tuple_item[0]:
                            # add the item with quantity into shopping cart located in global space
                            # item price quantity_placed
                            # after adding, print statement what and how many have been added into
                            # print your current total
                            value[tuple_item] += 1
                            print('** ' + str(value[tuple_item]) +
                                  ' order of ' + tuple_item[0] +
                                  ' have been added to your meal **')
                            sub_total()
                            print('{} {}'.format('Your current total is now: ',
                                  '$' + str(sub_total())))


def sub_total():
    """
    runs subtotal for receipt
    """
    total = 0.00
    for value in menus.values():
        for tuple_item, count in value.items():
            total += tuple_item[1] * count
    return total


def print_receipt():
    """
    prints receipt when user enters 'order'
    """
    subtotal = 0.0
    print('{} {}'.format('Order ', '#' + str(uuid.uuid4())))
    for value in menus.values():
        for tuple_item, count in value.items():
            if count > 0:
                item_total = tuple_item[1] * count
                subtotal += item_total
                item_total = '{0:.2f}'.format(item_total)
                receipt = '{} {:>2} {:>22}'.format(tuple_item[0], 'x' +
                                                   str(count), '$' +
                                                   str(item_total))
                print(receipt)
    # sales tax
    sales_tax = subtotal * 0.101
    total = subtotal + sales_tax
    subtotal_string = '{} {:>22}'.format('Subtotal', '$' +
                                         str(round(subtotal, 2)))
    sales_tax_string = '{} {:>22}'.format('Sales Tax', '$' +
                                          str(round(sales_tax, 2)))
    total_string = '{} {:>22}'.format('Total Due', '$' + str(round(total, 2)))
    receipt_string = '{}\n{}\n{}'.format(subtotal_string, sales_tax_string,
                                         total_string)
    print(receipt_string)
    return receipt_string


def ask_optional_menu():
    """
        ask user if they want to use their own menu written in csv
        if user input is no, print our own menu (menu_items())
        input: yes, no
        output: invoking the corresponding method
    """
    print("""Do you like to use your own menu (CSV only)?\n
    If you want, please type 'Yes'\n
    If you don't, please type 'No'""")
    user_input = input('>' + '\t')
    answer = user_input.title()
    # while True:
    if answer == 'Yes':
        ask_file_path()
    elif answer == 'No':
        menu_items()
    else:
        print('Please answer only with Yes or No!')


def ask_file_path():
    """ ask user to provide a path file """
    global menus
    print('Please provide a file path to menu.csv')
    file_path = input('>' + '\t')
    with open(file_path, newline='') as menu_csv:
        your_menu = csv.reader(menu_csv, delimiter=',')
        custom_menu = {}
        for row in your_menu:
            # read out each row and generate menus
            generate_menu(custom_menu, row)
        menus = custom_menu
        menu_items()


def generate_menu(custom_menu, arr):
    """This function creates custom_menu
    in dictionary (with nested dict containing tuples) """
    price = float(arr[2])
    qty = float(arr[3])
    if arr[1] in custom_menu.keys():
        print(arr[1])
        custom_menu[arr[1]][(arr[0], price)] = qty
    else:
        custom_menu[arr[1]] = {(arr[0], price): qty}


# calling functions


if __name__ == '__main__':
    menu_welcome()
    ask_optional_menu()
    # menu_items()
    ordering()
