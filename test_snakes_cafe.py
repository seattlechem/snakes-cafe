import snakes_cafe


def test_menu_welcome():
    assert snakes_cafe.menu_welcome() == """
            ****************************************
            **     Welcome to the Snakes Cafe!    **
            **  ********************************  **
            **   To quit at any time, Type 'quit' **
            ****************************************
           """


def test_sub_total():
    assert snakes_cafe.sub_total() == 0
