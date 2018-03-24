## Test Plan for snakes_cafe 03_21_18

# menu_welcome
        test for accurate string to be printed
        

# menu_items
        Output => string
        Test if menu_item output is type string and matches test record

# ordering
        ordering requires user input and for this lab Scott said to not test for user input (for this days lab only).


# sub_total
        Output => == 0 since we have no user input at time of test


# print_receipts
        Output (with no user input) => string of receipt print out with zero amounts
        input => coffee = 
        output => string of part of reciept

# ask_optional_menu
        user input => yes or no so no test available
        
# ask_file_path
        user input => no test possible

# generate_menu
        input => list 
        output => dict with nested dict containing tuples 

# generate_menu_filled
        input => manually created list
        output => dict vwith nested dict containing tuples
# item Check
        Item check tests true if item is in menu is true.
        item check tests false if item is in menu is false. 

# quantity check
        Item check tests true if test quantity matches amount in menu
        Item check tests False if test quantity  amount is greater then what is in menu  

# adding_item_to_cart
tests that an item added to cart is in cart
tests that an tiem is added twice via multiple lines
tests that an item is added for multiple qunatities via one line 
