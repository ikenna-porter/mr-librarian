import sqlite3

def create_reading_list_table():
    """Creates a table for the reading list."""
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

def create_recently_fetched_books():
    """Creates recently_fetched_books table that will store the most recent Google Books API response body."""
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
    """Adds the selected book to the recently_fetched_books table."""
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO recently_fetched_books VALUES (?, ?, ?, ?)", (book["id"], book["title"], book["authors"], book["publisher"]))

def add_book_to_reading_list(book):
    """Adds the selected book to the reading_list table."""
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO reading_list VALUES (?, ?, ?)", (book[1], book[2], book[3]))

def select_reading_list():
    """Prints reading_list table on the console."""
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reading_list")
    return c.fetchall()

def delete_recently_fetched_books():
    """Deletes the recently_fetched_books."""
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    with conn:
        c.execute("DROP TABLE recently_fetched_books")

def select_book_to_add(num):
    """Takes in a number (1-5) and selects the corresponding book from the recently_fetched_books table that is associated with the number."""
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    c.execute("SELECT * FROM recently_fetched_books WHERE id=?", (num))
    return c.fetchall()

def does_fetched_books_table_exist():
    """Checks if recently_fetched_books table exists. Will return a 0 if it does not and a 1 if it does."""
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    is_table_real = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='recently_fetched_books'")
    return len(is_table_real.fetchall())

def does_reading_list_table_exist():
    """Checks if reading_list table exists. Will return a 0 if it does not and a 1 if it does."""
    conn = sqlite3.connect("mr-librarian.db")
    c = conn.cursor()
    is_table_real = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='reading_list'")
    return len(is_table_real.fetchall())

def create_and_insert_in_recently_fetched_table(list_):
    """Creates the recently_fetched_books table and inserts all of the books from API response into the table."""
    create_recently_fetched_books()
    for book in list_:
        add_book_to_recently_fetched_list(book)
