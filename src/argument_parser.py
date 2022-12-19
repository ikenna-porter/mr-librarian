import argparse
from api_manager import APIManager

class ArgumentParser():
    """A class that accepts user's input, parses it, and decides what course of action to take based on input."""

    def argument_parser_configs():
        #create the top-level parser
        parser = argparse.ArgumentParser(description="Welcome to Mr. Librarian. Let's get reading!")
        subparsers = parser.add_subparsers()

        #establishes format for arguments to find a book
        #python main.py find-book -f <user input>
        find_book_parser = subparsers.add_parser("find-book", help="Finds books using Google Books API")
        find_book_parser.add_argument("-f", type=str, nargs="+")

        #establishes format for arguments to find a book
        #python main.py book-list --add 2
        #python main.py book-list --view
        book_list_parser = subparsers.add_parser("book-list", help="Adds book to reading list")
        book_list_parser.add_argument("--add", choices=["1","2","3","4","5"])
        book_list_parser.add_argument("--view", action="store_true", help="View your reading list")

        return  parser.parse_args()
    
    def parse_arguments(self, user_input):
        """Takes in user's input and decides what course of action the program should take."""
        args_dict = vars(user_input)
        print(args_dict)
        for arg in args_dict:
            print(arg)
            if args_dict[arg]:
                if arg == "f":
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