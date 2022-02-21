from File_management_Examples import fun_database

def menu():
    user_options = """
    Menu Option : 
    a - Add book
    b - Print book
    c - Delete book
    d - Mark as read
    q - Quit   
    Enter your choice : 
    """
    userinput = input(user_options).upper()

    while userinput != 'Q':
        if userinput == 'A':
            fun_database.add_book()
        elif userinput == 'B':
            fun_database.get_book()
        elif userinput == 'C':
            fun_database.delete_book()
        elif userinput == 'D':
            fun_database.read()
        else:
            print(" Wrong input , try again")
        userinput = input(user_options).upper()

menu()
