import snakes_cafe


def test_menu_welcome():
    assert snakes_cafe.menu_welcome() == """
            ****************************************
            **     Welcome to the Snakes Cafe!    **
            **  ********************************  **
            **   To quit at any time, Type 'quit' **
            ****************************************
           """


def test_menu_items():
    assert snakes_cafe.menu_items() == """
Appetizers----------
Wings,               $2.00
Cookies,              $15.00
Spring Rolls,               $4.00
Rings,               $4.00
Crab Dip,               $4.00
Sliders,               $4.00

Entrees----------
Salmon,               $5.00
Steak,               $6.00
Meat Tornado,               $4.00
A Literal Garden,               $3.00
Pasta,               $4.00
Ribs ,               $4.00

Desserts----------
Ice Cream,             $500.00
Cake ,              $30.00
Pie  ,               $3.00
Pudding,               $4.00
Fruit,               $4.00
Sorbet,               $4.00

Drinks----------
Coffee,               $4.00
Tea  ,               $3.00
Blood of the Innocent,               $6.00
Pop  ,               $4.00
Wine ,               $4.00
Beer ,               $4.00

Sides----------
Frys ,               $4.00
Salad,               $3.00
Bread,               $6.00
Slaw ,               $4.00
Soup ,               $4.00
Rice ,               $4.00
"""


def test_empty_print_receipt():
    assert """Subtotal                   $0.0
Sales Tax                   $0.0
Total Due                   $0.0""" in snakes_cafe.print_receipt()


def test_filled_print_receipt():
    snakes_cafe.menus['Drinks'][('Coffee', 4.00)] = 2
    assert """Subtotal                   $8.0
Sales Tax                  $0.81
Total Due                  $8.81""" in snakes_cafe.print_receipt()
    snakes_cafe.menus['Drinks'][('Coffee', 4.00)] = 0


def test_empty_sub_total():
    assert snakes_cafe.sub_total() == 0


def test_filled_sub_total():
    snakes_cafe.menus['Appetizers'][('Wings', 2.00)] = 5
    assert snakes_cafe.sub_total() == 10.00
    snakes_cafe.menus['Appetizers'][('Wings', 2.00)] = 0


def test_generate_menu():
    custom_menu = {}
    arr = ['Frys', 'Appetizer', 10, 54]
    snakes_cafe.generate_menu(custom_menu, arr)
    assert custom_menu == {'Appetizer': {('Frys', 10): 54}}


def test_generate_menu_filled():
    custom_menu = {'Dessert': {('Flan', 4): 34}}
    arr = ['Frys', 'Appetizer', 10, 54]
    snakes_cafe.generate_menu(custom_menu, arr)
    assert custom_menu == {'Dessert': {('Flan', 4): 34},
                           'Appetizer': {('Frys', 10): 54}}
