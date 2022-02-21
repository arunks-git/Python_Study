import sqlite3

def add_db_table():
    conn = sqlite3.connect('test_lib.db')
    cusr = conn.cursor()

    cusr.execute('CREATE TABLE books(name text primary key , author text , read text)')

    conn.commit()
    conn.close()

def add_book():
    name = input("Book name:")
    author = input("Book Author:")
    read = input("If Read (Yes or No):")

    conn = sqlite3.connect('test_lib.db')
    cusr = conn.cursor()

    cusr.execute('INSERT INTO books VALUES(? , ? , ?)', (name, author, read))

    conn.commit()
    conn.close()

def get_book():
    conn = sqlite3.connect('test_lib.db')
    cusr = conn.cursor()

    cusr.execute('SELECT * FROM books')
    books = [{'name' : row[0] ,'author' : row[1] , 'read' : row[2]} for row in cusr.fetchall()]

    conn.commit()
    conn.close()

    print(books)

def read():
    name = input("Enter name of book that is read :")

    conn = sqlite3.connect('test_lib.db')
    cusr = conn.cursor()

    cusr.execute('UPDATE books SET read="Yes" WHERE name=?',(name,))

    conn.commit()
    conn.close()

def delete_book():
    name = input("Enter name of book that need to be removed :")

    conn = sqlite3.connect('test_lib.db')
    cusr = conn.cursor()

    cusr.execute('DELETE FROM books WHERE name=?',(name,))

    conn.commit()
    conn.close()


