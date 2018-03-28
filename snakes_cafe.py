import csv
from uuid import uuid4


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


class Order:
    """Class for Order"""
    def __init__(self):
        self.id = str(uuid4())
        self.cart = {}

    def __len__(self):
        return len(self.cart())

    def main(self):
        flag = True
        while flag:
            user_input = self._order_prompt()
            flag = self._user_input_check(user_input)

    def add_item(self, item_name, quantity=1):
        if not item_check(item_name):
            return
        if quantity > 0:
            if not self._quantity_check(item_name, quantity):
                return
        # else:
        #     print('Your entered quantity is not valid.')
        #     return
            
        for key, value in menus.items():
            for tuple_item in value:
                if item_name == tuple_item[0]:
                    if tuple_item[0] in self.cart:
                        self.cart[tuple_item[0]]['quantity'] += quantity
                    else:
                        self.cart[tuple_item[0]] = {'price': tuple_item[1],
                                                    'quantity': quantity}
                    print('** {} order of {} have been added into your cart.\n\
                          Your current total is now: ${}'
                          .format(item_name, quantity,
                                  self._subtotal()))
                    break

    def remove_item(self, item_name, num=1):
        """remove item """
        for key in self.cart.keys():
            if item_name in key:
                if num == self.cart[key]['quantity']:
                    del self.cart[key]
                elif num > self.cart[key]['quantity'] or num < 0:
                    print('Please check your quantity.')
                else:
                    self.cart[key]['quantity'] -= num
                break
        print('The item is not in your order.')

    def display_order(self):
        subtotal = 0.0
        print('{} {} {} {}'.format('*' * 60, 'Order id: #' + self.id + '\n',
              'Thank you for visiting the Snakes Cafe!' + '\n', '*' * 60,))
        for item, info in self.cart.items():
            item_total = info['price'] * info['quantity']
            subtotal += item_total
            item_total = '{0:.2f}'.format(item_total)
            receipt = '{} {:>2} {:>22}'.format(item, 'x' +
                                               str(info['quantity']), '$' +
                                               str(item_total))
            print(receipt)
        # sales tax
        sales_tax = subtotal * 0.101
        total = subtotal + sales_tax
        subtotal_string = '{} {:>22}'.format('Subtotal', '$' +
                                             str(round(subtotal, 2)))
        sales_tax_string = '{} {:>22}'.format('Sales Tax', '$' +
                                              str(round(sales_tax, 2)))
        total_string = '{} {:>22}'.format('Total Due', '$' +
                                          str(round(total, 2)))
        receipt_string = '{}\n{}\n{}'.format(subtotal_string, sales_tax_string,
                                             total_string)
        print(receipt_string)
        return receipt_string

    def print_receipt(self):
        """save the current order as file."""
        receipt_string = self.display_order()
        a = ''
        a += receipt_string
        with open('receipts/' + self.id + '.txt', 'w') as f:
            f.write(a)

    def _remove_check(self, user_input):
        if ',' in user_input:
            user_input_item, quantity = user_input.split(', ', 1)
            if quantity.isdigit():
                self.remove_item(user_input_item, int(quantity))
            else:
                print('Please enter quantity in number.')
        else:
            self.remove_item(user_input)

    def _subtotal(self):
        subtotal = 0
        for item, info in self.cart.items():
            item_total = info['price'] * info['quantity']
            subtotal += item_total
        subtotal = '{0:.2f}'.format(subtotal)
        return subtotal

    def _order_prompt(self):
        order_prompt = '''
        What would you like to order?
        Please enter item name and quantity
        separated by a comma.
        Enter quit any time to exit.
        Enter "remove" if you want to
        remove an item.'''
        print('{}\n{}\n{}'.format('*' * 60, order_prompt, '*' * 60))
        user_input = input('>\t')
        user_input = user_input.title()
        return user_input

    def _quantity_check(self, item, qty):
        num = 0
        for value in menus.values():
            for tuple_item in value:
                if item == tuple_item[0]:
                    if qty > value[tuple_item]:
                        print("We don't have that many.")
                        return False
                    for key in self.cart.keys():
                        if item == key:
                            num = self.cart[item]['quantity']
                            if qty + num > value[tuple_item]:
                                print("We don't have that many")
                                return False
                            return True
                    return True
        return False

    def _user_input_check(self, user_input):
        if user_input == 'Quit':
            return False
        elif user_input == 'Order':
            self.print_receipt()
        elif user_input == 'Menu':
            menu_items()
        elif user_input == 'Remove':
            print('''
            Enter name of item and quantity that\
            you want to remove separated by comma.''')
            which_item_remove = input('>\t')
            which_item_remove = which_item_remove.title()
            self._remove_check(which_item_remove)
        elif user_input in menus.keys():
            print_sub_menu(user_input)
        else:
            if ',' in user_input:
                user_input_item, quantity = user_input.split(', ', 1)
                if quantity.isdigit():
                    self.add_item(user_input_item, int(quantity))
                else:
                    print('Please enter number.')
            else:
                self.add_item(user_input)
        return True


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


def print_sub_menu(str):
    for key, value in menus.items():
        if str == key:
            for item in value.keys():
                print(item[0])
                return item[0]


# item check
def item_check(item_name):
    for value in menus.values():
        if item_name in [key[0] for key in value]:
            return True
    print("We don't have that item.")
    return False


# quantity check
# def quantity_check(num):
#     global user_input
#     user_input = user_input.title()
#     item_name = user_input.split(', ')[0]
#     for value in menus.values():
#         for tuple_item in value:
#             if item_name == tuple_item[0]:
#                 if num > value[tuple_item]:
#                     print("We don't have that many.")
#                     return False
#                 if item_name in self.cart
#                 return True
#     return False


# new function (test needed)
# def adding_item_to_cart(self, item_name, num_of_item=1):
#     prev_num = 0
#     for key, value in menus.items():
#         for tuple_item in value:
#             if item_name == tuple_item[0]:
#                 if tuple_item[0] in self.cart:
#                     prev_num = self.cart[tuple_item[0]][tuple_item[1]]
#                     self.cart[tuple_item[0]].update({tuple_item[1]:
#                                                      prev_num + num_of_item})
#                     break
#                 else:
#                     self.cart[tuple_item[0]] = {tuple_item[1]: num_of_item}
#                     break
#     return self.cart


def sub_total(self):
    """
    runs subtotal for receipt
    """
    total = 0.00
    for value in self.cart.values():
        for item_price, count in value.items():
            total += item_price * count
    return total


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
    try:
        with open(file_path, newline='') as menu_csv:
            your_menu = csv.reader(menu_csv, delimiter=',')
            custom_menu = {}
            for row in your_menu:
                generate_menu(custom_menu, row)
            menus = custom_menu
            menu_items()
    except FileNotFoundError:
        raise FileNotFoundError('You file cannot be found. Please check your file')


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
    new_order = Order()
    menu_welcome()
    ask_optional_menu()
    menu_items()
    new_order.main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Thank you for visiting snakes cafe.")
