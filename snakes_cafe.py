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
    print('*' * 40)
    print(('*' * 2) + '     Welcome to the Snakes Cafe!    ' + ('*' * 2))
    print(('*' * 2) + ' ' * 36 + ('*' * 2))
    print(('*' * 2) + '  To quit at any time, type "quit"  ' + ('*' * 2))
    print('*' * 40)


def menu_items():
    for key, value in menus.items():
        print(key)
        print('-' * 10)
        for tuple_item in value:
            print('{:>22}, {:>22}'.format(tuple_item[0],
                  '$' + str(tuple_item[1])))


# menu_items()


def ordering():
    condition = True
    print(('*' * 40) + '\n' + ('*' * 2) +
          'What would you like to order?  ' + ('*' * 2) + '\n' +
          ('*' * 40) + '\n' + 'Enter quit any time to exit')
    while condition:
            order = input('>' + '\t')
            order = order.title()
            if order == 'Quit':
                condition = False
                break
            else:
                for _, value in menus.items():
                    for tuple_item, count in value.items():                   
                        if order == tuple_item[0]:
                            value[tuple_item] += 1
                            print('** ' + str(value[tuple_item]) +
                                  ' order of ' + tuple_item[0] +
                                  ' have been added to your meal **')
                            sub_total()
                            print('{} {}'.format('Your current total is now: ', '$' + str(sub_total())))
                        elif order == 'Order'
                            


def sub_total():
    total = 0.0
    for _, value in menus.items():
        # print(key, value)
        for tuple_item, count in value.items():
            # print(tuple_item[1], count)
            total += tuple_item[1] * count
    return total

# menu_welcome()


menu_items()
ordering()



