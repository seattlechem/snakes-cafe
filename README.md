# snakes-cafe
Snakes Cafe restaurant Lab 1

# snakes-cafe
Snakes Cafe restaurant Lab 1

**Author**: Peter Kim and Jay Adams
**Version**: 1.4.0 

## Overview
Ordering system for the Snakes Resturant that allows users to see a menu and create orders.

## Getting Started
Download the source code and relevant dependencies, navigate to the relevant downloads folder, and execute the script using the command: python3 snakes_cafe.py You can exit the program by 'quit" at any time.

## Architecture
written in Python3.6.4 within a virtual enviornment. 

## API
No APIs were consumed by this app.

## Custom Menu
The menu can be substituted by user's custom menu. The custom menu should be in csv file format, and each row should be separated by comma in order of item_name, category_name, price, and stock_quantity.

## Change Log
(1.4.0) for remove_item, instead of priting it's changed to return string
(1.4.0) intead of print, it is saved as string and returned to the method when it was invoked.
(1.4.0) self.cart is not method/function it didn't need to be called and it is fixed now for testing.
(1.4.0) test for menu_items() complete
(1.4.0) custom menu information is added into README.md
(1.4.0) remove method is refactored
(1.4.0) adding to cart function is deleted. items are added by Order class method
(1.4.0) _quantity_check method is refactored now it checks quantity in cart
(1.4.0) try except FileNotFound clause is added for opening csv file not exist
(1.4.0) comma check method was added
(1.4.0) class Order and methods (including help methods) created
(1.3.0) aa40e81 menus updated
(1.3.0) f0d093d Merge branch 'class_03_robust' of https://github.com/seattlechem/snakes-cafe into class_03_robust
(1.3.0) e8cf185 added test cases for generate_menu() / update test_plan.md / refactored ask_file_path()
(1.3.0) 2479355 updated readme.md
(1.3.0) b8b71d2 test completed for print receipt when ordering two coffee
(1.3.0) 503b600 test completed for sub_total() when items are ordered
(1.3.0) a2fa899 test case completed for print_receipt()
(1.3.0) 3066c47 menu_items() was refactored
(1.3.0) ef645e0 fixed remove item function so that it prints receipt after order
(1.3.0) 9749573 Merge pull request #2 from seattlechem/class-02-tdd
