books = []
books1 = []

def add_book():
    name = input("Book name : ")
    author = input("Book Author : ")
    read = input("If Read (Yes or No) : ")
    books.append({'Name': name , 'author': author , 'READ': read})


def get_book():
    for book in books:
        print(book)

def delete_book():
    global books
    name = input("Enter name of book to be deleted : ")
    for book in books:
        if book['Name'] != name:
            books1.append(book)
    books = books1

def read():
    name = input("Enter name of book that is read : ")
    for book in books:
        if book['Name'] == name:
            book['READ'] = 'Yes'
            print(f" {book['Name']} Marked as Read")