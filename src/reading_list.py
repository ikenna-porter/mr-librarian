import queries
from sqlite3 import OperationalError
from tabulate import tabulate
class ReadingList():
    """A class that represents a list of books the user wants to read."""

    def add_book(self, num):
        """Adds books to the reading list."""
        try:
            if queries.does_reading_list_table_exist() == 1:
                book = queries.select_book_to_add(num)
                queries.add_book_to_reading_list(book[0])
                print("\n*Book successfully added*\n")
                self.view_list()
            else:
                print(queries.does_reading_list_table_exist())
                queries.create_reading_list_table()
                book = queries.select_book_to_add(num)
                queries.add_book_to_reading_list(book[0])
                print("\n*Book successfully added*\n")
                self.view_list()
        except OperationalError as e:
            print("Silly, you can't add a nonexistent book to your reading list. Run 'python main.py find-book -f <search query>' first.")
            print(e)

    def view_list(self):
        """Displays the user's reading list in the console."""
        list = queries.select_reading_list()
        print("\nYOUR READING LIST:\n")
        print(tabulate(list, headers=["Title", "Author(s)", "Publisher"], tablefmt="simple"), "\n")
