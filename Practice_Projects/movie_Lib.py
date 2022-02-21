def view(mov):
    print("Movie Name       Lang")
    for m in mov:
        print(f" {m['Name']}            {m['Lang']}")

def add_movie(mov):
    print(mov)
    name_new = input(" New Movie name : ")
    lang_new = input(" New Movie language : ")
    new_entry = { "Name": name_new , "Lang": lang_new }
    mov.append(new_entry)
    return mov

def search(mov):
    search_word = input("Enter movie to search : ")
    for m in mov:
        if m["Name"] == search_word:
            print("Please find details : ")
            print(m)
            break
    else:
        print("Not found")

def menu(movie):

    print(" Menu Options :  \n 1. View Movie list \n 2. Add a Movie \n 3. Search a Movie \n 4. Quit ")
    command = input("Enter the option : ")
    while command != "4":
        if command == "1":
            view(movie)
            break
        elif command == "2":
            movie = add_movie(movie)
            print(movie)
            break
        elif command == "3":
            search(movie)
            break
        else:
            print("Wrong Option")
            break
    cont = input(" Type Y to continue : ")
    if cont == "Y":
        menu(movie)
    else:
        print("Exiting")


movie = [{"Name": "XXXX", "Lang": "ENG"},
            {"Name": "YYYY", "Lang": "KOR"},
             {"Name": "ZZZZ", "Lang": "FRN"}]
menu(movie)




