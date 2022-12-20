import sqlite3

def create_reading_list_table():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE reading_list
            title text,
            author text,
            publisher text;
        )""")
    conn.commit()
    conn.close()

#create recently_fetched_books books table
def create_recently_fetched_books():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE recently_fetched_books (
            title text,
            author text,
            publisher text;
        )""")

def add_book_to_reading_list(book):
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO reading_list VALUES (?, ?, ?)", (book.title, book.author, book.publisher))

def show_reading_list():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reading_list")
    return c.fetchall()

def delete_recently_fetched_book():
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    with conn:
        c.execute("DROP TABLE recently_fetched_books")

def select_book_to_add(num):
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("SELECT * FROM recently_fetched_books WHERE id=?", (num))
    return c.fetchall()

