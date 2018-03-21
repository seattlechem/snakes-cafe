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


def test_sub_total():
    assert snakes_cafe.sub_total() == 0


def test_print_receipt():
    assert """ubtotal                   $0.0
Sales Tax                   $0.0
Total Due                   $0.0""" in snakes_cafe.print_receipt()


