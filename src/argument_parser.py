import argparse
import os, sys
from .reading_list import ReadingList

#prevents relative import issues running unit tests
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.api_manager import APIManager

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
        #python main.py reading-list --add 2
        #python main.py reading-list --view
        book_list_parser = subparsers.add_parser("reading-list", help="Adds book to reading list")
        book_list_parser.add_argument("-a", choices=["1","2","3","4","5"])
        book_list_parser.add_argument("-v", action="store_true", help="View your reading list")

        return parser.parse_args()
    
    def parse_arguments(self, user_input):
        """Takes in user's input and decides what course of action the program should take."""
        args_dict = vars(user_input)
        for arg in args_dict:
            if args_dict[arg]:
                if arg == "f":
                    search_query = self.parse_find_books_arg(args_dict["f"])

                    fetch_data = APIManager()
                    books = fetch_data.fetch_books(search_query)
                    return ["f", books]

                elif arg == "a":
                    return["a", args_dict[arg]]

                elif arg == "v":
                    return["v"]
                else:
                    print("Invalid argument. Please type 'python main.py --help' for guidance.")
    
    def parse_find_books_arg(self, args_list):
        """Formats query so that it can be read by Google Book's API"""
        if len(args_list) == 0:
            raise IndexError("Your search query must contain characters. Insert them after the '-f' flag.")

        return "+".join(args_list)


    def parse_add_book_arg(self):
        pass