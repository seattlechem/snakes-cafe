

import uuid

menus = {'Appetizers': {('Wings', 2.00): 0, ('Cookies', 15.00): 0,
         ('Spring Rolls', 4.00): 0, ('Rings', 4.00): 0,
         ('Crab Dip', 4.00): 0, ('Sliders', 4.00): 0},
         'Entrees': {('Salmon', 5.00): 0, ('Steak', 6.00): 0,
                     ('Meat Tornado', 4.00): 0, ('A Literal Garden', 3.00): 0,
                     ('Pasta', 4.00): 0, ('Ribs', 4.00): 0},
         'Desserts': {('Ice Cream', 500.0): 0, ('Cake', 30.00): 0,
                      ('Pie', 3.00): 0, ('Pudding', 4.00): 0,
                      ('Fruit', 4.00): 0, ('Sorbet', 4.00): 0},
         'Drinks': {('Coffee', 4.00): 0, ('Tea', 3.00): 0,
                    ('Blood of the Innocent', 6.00): 0, ('Pop', 4.00): 0,
                    ('Wine', 4.00): 0, ('Beer', 4.00): 0},
         'Sides': {('Frys', 4.00): 0, ('Salad', 3.00): 0,
                   ('Bread', 6.00): 0, ('Slaw', 4.00): 0, ('Soup', 4.00): 0,
                   ('Rice', 4.00): 0}}


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
    for key, value in menus.items():
        print(key)
        print('-' * 10)
        for tuple_item in value:
            price = '{0:.2f}'.format(tuple_item[1])
            print('{:<5}, {:>20}'.format(tuple_item[0],
                  '$' + str(price)))


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
    for _, value in menus.items():
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
    print('{} {:>22}'.format('Subtotal', '$' + str(round(subtotal, 2))))
    print('{} {:>22}'.format('Sales Tax', '$' + str(round(sales_tax, 2))))
    print('{} {:>22}'.format('Total Due', '$' + str(round(total, 2))))


# calling functions


if __name__ == '__main__':
    menu_welcome()
    menu_items()
    ordering()
