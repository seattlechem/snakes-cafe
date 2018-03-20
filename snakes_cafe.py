if __name__ == '__main__':

    menus = {'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
            'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0,
                        'A Literal Garden': 0},
            'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
            'Drinks': {'Coffee': 0, 'Tea': 0, 'Blood of the Innocent': 0}}

    print("""
    ****************************************
    **    Welcome to the Snakes Cafe!     **
    **  ********************************  **
    **  To quit at any time, type "quit"  **
    ****************************************
    """)

    # def menu_welcome():
    #     print('*' * 40)
    #     print(('*' * 2) + '     Welcome to the Snakes Cafe!    ' + ('*' * 2))
    #     print(('*' * 2) + ' ' * 36 + ('*' * 2))
    #     print(('*' * 2) + '  To quit at any time, type "quit"  ' + ('*' * 2))
    #     print('*' * 40)




    def menu_items():
        for key, value in menus.items():
            print(key)
            print('-' * 10)
            for item in value:
                print(item)
            print()    


    menu_items()



    def ordering():
        condition = True
        print(('*' * 40) + '\n' + ('*' * 2) +
                    '  What would you like to order?  ' + ('*' * 2) + '\n' +
                    ('*' * 40) + '\n' + 'Enter quit any time to exit' )
        while condition == True:
                order = input('>' + '\t')
                order = order.title()
                if order == 'Quit':
                    condition = False
                    break
                else:
                        for _, order_count in menus.items():
                            for item in order_count:
                                if order == item:
                                    order_count[item] += 1
                                    print('** ' + str(order_count[item])+ ' order of ' + item + ' have been added to your meal **') 
                    
                
        

    #menu_welcome()

    menu_items()
    ordering()


