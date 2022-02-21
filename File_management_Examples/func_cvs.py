book_file = 'Book_details.txt'

def add_book():
    name = input("Book name : ")
    author = input("Book Author : ")
    read = input("If Read (Yes or No) : ")
    with open(book_file , 'a' ) as book:
        book.write(f"{name},{author},{read}\n")

def get_book():
    with open(book_file, 'r' ) as book:
        book_value = [ line.strip().split(',') for line in book.readlines() ]

    return [{'Name': line[0],'Author' : line[1] , 'Read': line[2] }
                for line in book_value ]

def _save_file(book_to_save):
    with open(book_file , 'w' ) as book:
        for book1 in book_to_save:
            book.write(f"{book1['Name']},{book1['Author']},{book1['Read']}\n")

def delete_book():
    book_value = get_book()
    name = input("Enter name of book to be deleted : ")
    books = [book for book in book_value if book['Name'] != name]
    _save_file(books)

def read():
    name = input("Enter name of book that is read : ")
    book_value = get_book()
    for book in book_value:
        if book['Name'] == name:
            book['Read'] = 'Yes'
    _save_file(book_value)
