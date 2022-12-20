import queries
from sqlite3 import OperationalError
class ReadingList():

    def add_book(self, num):
        try:
            book = queries.select_book_to_add(num)
            queries.add_book_to_reading_list(book)
            self.view_list()
        except OperationalError as e:
            print("You must find books to add to your reading list, before you try to add them. Run 'python main.py find-book -f <user input>' first")
            print(e)

    def view_list(self):
        list = queries.show_reading_list()
        print(list)
