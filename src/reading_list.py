import queries
from sqlite3 import OperationalError
class ReadingList():
    """A list of books the user wants to read"""

    def add_book(self, num):
        """A class that adds books to the reading list"""
        # try:
        if queries.does_reading_list_table_exist() == 1:
            book = queries.select_book_to_add(num)
            queries.add_book_to_reading_list(book[0])
            self.view_list()
        else:
            print(queries.does_reading_list_table_exist())
            queries.create_reading_list_table()
            book = queries.select_book_to_add(num)
            queries.add_book_to_reading_list(book[0])
            self.view_list()
        # except OperationalError as e:
        #     print("Silly, you can't add a nonexistent book to your reading list. Run 'python main.py find-book -f <search query>' first")
        #     print(e)

    def view_list(self):
        """Displays the user's reading list in the console."""
        list = queries.show_reading_list()
        print(list)
