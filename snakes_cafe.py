
import csv
import uuid

menus = {'Appetizers': {('Wings', 2.00): 3, ('Cookies', 15.00): 3,
         ('Spring Rolls', 4.00): 3, ('Rings', 4.00): 3,
         ('Shrimp bites', 4.00): 3, ('Wontons', 4.00): 3,
         ('Crab Dip', 4.00): 3, ('Sliders', 4.00): 3,
         ('Clams', 8.00): 3},
         'Entrees': {('Salmon', 5.00): 3, ('Steak', 6.00): 3,
                     ('Meat Tornado', 4.00): 3, ('A Literal Garden', 3.00): 3,
                     ('Pasta', 4.00): 3, ('Ribs', 4.00): 3,
                     ('Cabbage Rolls', 8.00): 3, ('Pizza', 4.00): 3,
                     ('Paella', 4.00): 3},
         'Desserts': {('Ice Cream', 500.0): 3, ('Cake', 30.00): 3,
                      ('Pie', 3.00): 3, ('Pudding', 4.00): 3,
                      ('Fruit', 4.00): 3, ('Sorbet', 4.00): 3,
                      ('Torte', 4.00): 3, ('Flan', 4.00): 3,
                      ('Apple', 4.00): 3},
         'Drinks': {('Coffee', 4.00): 3, ('Tea', 3.00): 3,
                    ('Blood of the Innocent', 6.00): 3, ('Pop', 4.00): 3,
                    ('Wine', 4.00): 3, ('Beer', 4.00): 3,
                    ('Sake', 4.00): 3, ('Cocoa', 4.00): 3,
                    ('Evian', 4.00): 3},
         'Sides': {('Frys', 4.00): 3, ('Salad', 3.00): 3,
                   ('Bread', 6.00): 3, ('Slaw', 4.00): 3, ('Soup', 4.00): 3,
                   ('Rice', 4.00): 3, ('Spinach', 4.00): 3,
                   ('Sauce', 4.00): 3, ('Crab dip', 4.00): 3}}

cart = {}


user_input = ''


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
    global user_input
    condition = True
    order_string = 'What would you like to order?'
    order_string2 = 'Please enter item name and quantity separated by a comma.'
    order_string3 = 'Enter quit any time to exit.'
    order_string4 = 'Enter "remove" if you want to remove an item.'
    print('{} {} {} {}'.format(order_string, order_string2,
                               order_string3, order_string4))
    while condition:
        user_input = input('>' + '\t')
        user_input = user_input.title()
        if ',' in user_input:
            user_input_item, quantity = user_input.split(', ', 1)
            # check if qty is not negative or string
            if quantity.isdigit() and int(quantity) > 0:
                # check stock quantity if valid
                user_input_qty = int(quantity)
                if not quantity_check(user_input_qty):
                    continue
            else:
                print('Your entered quantity is not valid.')
                continue
        else:
            user_input_item = user_input
            user_input_qty = 1
        if user_input_item == 'Quit':
            condition = False
            break
        elif user_input_item == 'Order':
            print_receipt()
        elif user_input_item == 'Remove':
            print('Enter name of item that you want to remove')
            which_item_remove = input('>' + '\t')
            which_item_remove = which_item_remove.title()
            for key in cart.keys():
                if which_item_remove in key:
                    del cart[key]
                    continue
            print('The item is not in your order.')
            continue
        elif user_input_item == 'Menu':
            menu_items()
        elif user_input_item in menus.keys():
            for key, value in menus.items():
                if user_input_item == key:
                    for key in value.keys():
                        print(key[0])
        else:
            if not item_check(user_input_item):
                continue
            adding_item_to_cart(user_input_item, user_input_qty)
            print('** {} order of {} have been added'
                  .format(user_input_qty, user_input_item))
            print('Your current total is now: ${}'
                  .format(str(sub_total())))


# item check
def item_check(item_name):
    for value in menus.values():
        if item_name in [key[0] for key in value]:
            return True
    print("We don't have that item.")
    return False


# quantity check
def quantity_check(num):
    global user_input
    user_input = user_input.title()
    item_name = user_input.split(', ')[0]
    for value in menus.values():
        for tuple_item in value:
            if item_name == tuple_item[0]:
                if num > value[tuple_item]:
                    print("We don't have that many.")
                    return False
                return True
    return False


# new function (test needed)
def adding_item_to_cart(item_name, num_of_item=1):
    prev_num = 0
    for key, value in menus.items():
        for tuple_item in value:
            if item_name == tuple_item[0]:
                if tuple_item[0] in cart:
                    prev_num = cart[tuple_item[0]][tuple_item[1]]
                    cart[tuple_item[0]].update({tuple_item[1]:
                                                prev_num + num_of_item})
                    break
                else:
                    cart[tuple_item[0]] = {tuple_item[1]: num_of_item}
                    break
    return cart


def sub_total():
    """
    runs subtotal for receipt
    """
    total = 0.00
    for value in cart.values():
        for item_price, count in value.items():
            total += item_price * count
    return total


def print_receipt():
    """
    prints receipt when user enters 'order'
    """
    global cart
    subtotal = 0.0
    print('{} {}'.format('Order ', '#' + str(uuid.uuid4())))
    for item, info in cart.items():
        for cost, qty in info.items():
            item_total = cost * qty
            subtotal += item_total
            item_total = '{0:.2f}'.format(item_total)
            receipt = '{} {:>2} {:>22}'.format(item, 'x' +
                                               str(qty), '$' +
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
    if not file_path.endswith('.csv'):
        print("It's not a csv file.")
        menu_items()
        return
    with open(file_path, newline='') as menu_csv:
        your_menu = csv.reader(menu_csv, delimiter=',')
        custom_menu = {}
        for row in your_menu:
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


def main():
    menu_welcome()
    ask_optional_menu()
    ordering()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Thank you for visiting snakes cafe.")
