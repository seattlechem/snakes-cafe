import snakes_cafe
import pytest

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
Shrimp bites,               $4.00
Wontons,               $4.00
Crab Dip,               $4.00
Sliders,               $4.00
Clams,               $8.00

Entrees----------
Salmon,               $5.00
Steak,               $6.00
Meat Tornado,               $4.00
A Literal Garden,               $3.00
Pasta,               $4.00
Ribs ,               $4.00
Cabbage Rolls,               $8.00
Pizza,               $4.00
Paella,               $4.00

Desserts----------
Ice Cream,             $500.00
Cake ,              $30.00
Pie  ,               $3.00
Pudding,               $4.00
Fruit,               $4.00
Sorbet,               $4.00
Torte,               $4.00
Flan ,               $4.00
Apple,               $4.00

Drinks----------
Coffee,               $4.00
Tea  ,               $3.00
Blood of the Innocent,               $6.00
Pop  ,               $4.00
Wine ,               $4.00
Beer ,               $4.00
Sake ,               $4.00
Cocoa,               $4.00
Evian,               $4.00

Sides----------
Frys ,               $4.00
Salad,               $3.00
Bread,               $6.00
Slaw ,               $4.00
Soup ,               $4.00
Rice ,               $4.00
Spinach,               $4.00
Sauce,               $4.00
Crab dip,               $4.00
"""


def test_empty_print_receipt():
    assert """Subtotal                   $0.0
Sales Tax                   $0.0
Total Due                   $0.0""" in snakes_cafe.print_receipt()


def test_empty_sub_total():
    assert snakes_cafe.sub_total() == 0.00


def test_filled_print_receipt():
    snakes_cafe.adding_item_to_cart('Coffee', 2)
    assert """Subtotal                   $8.0
Sales Tax                  $0.81
Total Due                  $8.81""" in snakes_cafe.print_receipt()
    snakes_cafe.cart = {}


def test_filled_sub_total():
    snakes_cafe.adding_item_to_cart('Coffee', 2)
    assert snakes_cafe.sub_total() == 8.00
    snakes_cafe.cart = {}


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


def test_item_check_true():
    """
    Tests that item is in menu is True
    """
    assert snakes_cafe.item_check('Soup') is True


def test_item_check_false():
    """
    Tests that item is in menu is False
    """
    assert snakes_cafe.item_check('Glue') is False


def test_quanity_check_true():
    """
    Tests that valaue in menus is true
    """
    print(snakes_cafe.user_input)
    snakes_cafe.user_input = 'Wings'
    assert snakes_cafe.quantity_check(3) is True


def test_quanity_check_false():
    """
    Tests that valaue in menus is false
    """
    snakes_cafe.user_input = "Wings"
    assert snakes_cafe.quantity_check(25) is False


def test_adding_item_to_cart():
    """
    Test if item added to cart
    """


def test_add_to_cart():
    """
    Tests that items that are in the menu
    but not in the cart are added to the cart
    """
    snakes_cafe.adding_item_to_cart('Wings')
    assert 'Wings' in snakes_cafe.cart
    snakes_cafe.cart = {}


def test_add_to_cart_add_one():
    """
    Tests that items that are in the menu
    but not in the cart are added to the cart
    """
    snakes_cafe.adding_item_to_cart('Wings')
    snakes_cafe.adding_item_to_cart('Wings')
    assert snakes_cafe.cart['Wings'][2.00] == 2
    snakes_cafe.cart = {}


def test_add_to_cart_five():
    """
    Tests that items that are in the menu
    but not in the cart are added to the cart
    """
    snakes_cafe.adding_item_to_cart('Wings',5)
    assert snakes_cafe.cart['Wings'][2.00] == 5
    snakes_cafe.cart = {}


