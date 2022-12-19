import argparse
from api_manager import APIManager

class ArgumentParser():
    """A class that accepts user's input, parses it, and decides what course of action to take based on input."""

    def argument_parser_configs():
        # """Establishes what arguments are acceptable for the application."""
        # parser = argparse.ArgumentParser(description="Welcome to Mr. Librarian. Let's get reading!")
        # parser.add_argument("--find-book", help="Find a book from Google Books")
        # parser.add_argument("--add-book", choices=["1","2","3","4","5"], help="Add a book to your reading list")
        # parser.add_argument("--view-list", action="store_true", help="View your reading list")
        # return  parser.parse_args()

        parser = argparse.ArgumentParser(description="Welcome to Mr. Librarian. Let's get reading!")
        subparser = parser.add_argument("--find-book", help="Find a book from Google Books")
        subparser.add_argument
        parser.add_argument("--add-book", choices=["1","2","3","4","5"], help="Add a book to your reading list")
        parser.add_argument("--view-list", action="store_true", help="View your reading list")
        return  parser.parse_args()
    
    def parse_arguments(self, user_input):
        """Takes in user's input and decides what course of action the program should take."""
        args_dict = vars(user_input)
        for arg in args_dict:
            print(arg)
            if args_dict[arg]:
                if arg == "find_book":
                    self.parse_find_books_arg(arg)

                    books = APIManager()
                    books.fetch_books()
                elif arg == "add_book":
                    print("Book added to reading list")
                elif arg == "view_list":
                    print("Snapshot of reading list")
                else:
                    print("Invalid argument. Please type 'python main.py --help' for guidance.")
    
    def parse_find_books_arg(self, arg):
        print(f'book found successfully? + {arg}')

    def parse_add_book_arg(self):
        pass