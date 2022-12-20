import sqlite3

def create_reading_list_table():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE reading_list (
            title text,
            author text,
            publisher text
        )""")
    conn.commit()
    conn.close()

#create recently_fetched_books books table
def create_recently_fetched_books():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE recently_fetched_books (
            id integer,
            title text,
            author text,
            publisher text
        )""")

def add_book_to_recently_fetched_list(book):
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO recently_fetched_books VALUES (?, ?, ?, ?)", (book["id"], book["title"], book["authors"], book["publisher"]))

def add_book_to_reading_list(book):
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO reading_list VALUES (?, ?, ?)", (book[1], book[2], book[3]))

def show_reading_list():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reading_list")
    return c.fetchall()

def delete_recently_fetched_books():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    with conn:
        c.execute("DROP TABLE recently_fetched_books")

def select_book_to_add(num):
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("SELECT * FROM recently_fetched_books WHERE id=?", (num))
    return c.fetchall()

#returns 0 if not exist and 1 if exist
def does_fetched_books_table_exist():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    return len(c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{recently_fetched_books}'").fetchall())

#returns 0 if not exist and 1 if exist
def does_reading_list_table_exist():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    return len(c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{reading_list}'").fetchall())

def create_and_insert_in_recently_fetched_table(list_):
    create_recently_fetched_books()
    for book in list_:
        add_book_to_recently_fetched_list(book)
