import sqlite3

conn = sqlite3.connect("mr-librarian.db")

c = conn.cursor()

#creates a book list table
c.execute("""
    CREATE TABLE book_list (
        title text,
        author text,
        publisher text
    )""")

#inserts data into book_list table
c.execute("INSERT INTO book_list VALUES()") #add values in order

#renders book_list table
c.execute("SELECT * FROM book_list")

#create recently_fetched_books books table
c.execute("""
    CREATE TABLE recently_fetched_books (
        title text,
        author text,
        publisher text
    )""")

conn.commit()
conn.close()