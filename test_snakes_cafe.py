import snakes_cafe
import pytest


@pytest.fixture
def empty_order():
    return snakes_cafe.Order()


@pytest.fixture
def cart_3_wings():
    order_obj = snakes_cafe.Order()
    order_obj.add_item('Wings', 3)
    return order_obj


def test_menu_welcome():
    ''' This tests the printout of welcome message '''
    assert snakes_cafe.menu_welcome() == """
            ****************************************
            **     Welcome to the Snakes Cafe!    **
            **  ********************************  **
            **   To quit at any time, Type 'quit' **
            ****************************************
           """


def test_menu_items():
    ''' This tests the printout of menu items'''
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


def test_len_order_class(empty_order):
    ''' This tests the length of empty Order object is 0 '''
    assert len(empty_order) == 0


def test_add_item(empty_order):
    ''' This tests the printout when adding 3 Wings into cart'''
    assert empty_order.add_item('Wings', 3) == '** 3 order of Wings have been added to your cart.\n\
                          Your current total is now: $6.00'


def test_remove_item(cart_3_wings):
    '''This tests the printout when removing 1 wing from the cart (cart has 3
       wings before remove is called) '''
    assert cart_3_wings.remove_item('Wings', 1) == '1 order \
of Wings is removed.'


def test_display_order(cart_3_wings):
    ''' This tests the prinout when display_order method is invoked when there\
    are 3 Wings in the cart. It confirms that Total Due is same.'''
    assert '''
Total Due                  $6.61''' in cart_3_wings.display_order()


def test_subtotal(cart_3_wings):
    ''' This tests validation of subtotal when there are
    3 wings in the cart '''
    assert cart_3_wings._subtotal() == '6.00'


def test_quantity_check(empty_order):
    ''' This tests if it returns False when checking
    if 6 Wings can be ordered.'''
    assert empty_order._quantity_check('Wings', 6) is False


def test_generate_menu():
    ''' This tests the validation of generating custom menu'''
    custom_menu = {}
    arr = ['Frys', 'Appetizer', 10, 54]
    snakes_cafe.generate_menu(custom_menu, arr)
    assert custom_menu == {'Appetizer': {('Frys', 10): 54}}


def test_generate_menu_filled():
    ''' This test the validation of adding additional
    menu items into the pre-existing menu'''
    custom_menu = {'Dessert': {('Flan', 4): 34}}
    arr = ['Frys', 'Appetizer', 10, 54]
    snakes_cafe.generate_menu(custom_menu, arr)
    assert custom_menu == {'Dessert': {('Flan', 4): 34},
                           'Appetizer': {('Frys', 10): 54}}
