import argparse
import os, sys
import re as _re
OPTIONAL = '?'
ONE_OR_MORE = '+'
from gettext import gettext as _, ngettext

# Prevents relative import issues while running unit tests and while running main.py
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.api_manager import APIManager

class ArgumentParser(argparse.ArgumentParser):
    """A class that accepts user's input, parses it, and decides what course of action to take based on input."""

    def argument_parser_configs(self):
        """Creates the top-level parser using argparse library"""
        # parser = argparse.ArgumentParser(description="Welcome to Mr. Librarian. Let's get reading!")
        parser = self
        subparsers = parser.add_subparsers()

        # Establishes the format of the command line argument to find a book from Google Books API
        find_book_parser = subparsers.add_parser("find-book", help="Finds books using Google Books API")
        find_book_parser.add_argument("-f", type=str, nargs="+")

        # Establishes the format of the command line arguments to add book to reading list and to view the reading list
        book_list_parser = subparsers.add_parser("reading-list", help="Adds and views books to reading list")
        book_list_parser.add_argument("-a", help="Adds book to reading list by selecting its ID (1-5)", choices=["1","2","3","4","5"])
        book_list_parser.add_argument("-v", action="store_true", help="Views your reading list")

        return parser.parse_args()
    
    # parse_args() and print_usage() are both overridden methods from the parent class.
    # Overriding these methods allowed for error message customization (include print statement)
    def parse_args(self, args=None, namespace=None):
        args, argv = self.parse_known_args(args, namespace)
        if argv:
            print(f"\nInvalid argument. Please type 'python main.py --help' for guidance.")
            msg = _('unrecognized arguments: %s')
            self.error(msg % ' '.join(argv))
        return args
    
    def print_usage(self, file=None):
        self._print_message('')
    
    # def _match_argument(self, action, arg_strings_pattern):
    #     # match the pattern for this action to the arg strings
    #     nargs_pattern = self._get_nargs_pattern(action)
    #     match = _re.match(nargs_pattern, arg_strings_pattern)

    #     # raise an exception if we weren't able to find a match
    #     if match is None:
    #         nargs_errors = {
    #             None: _('expected one argument'),
    #             OPTIONAL: _('expected at most one argument'),
    #             ONE_OR_MORE: _('expected at least one argument'),
    #         }
    #         msg = nargs_errors.get(action.nargs)
    #         if msg is None:
    #             msg = ngettext('expected %s argument',
    #                            'expected %s arguments',
    #                            action.nargs) % action.nargs
    #         print(action)
    #         print("**********************************")
    #         print(msg)
    #         raise self.ArgumentError(action, msg)
    
    def parse_arguments(self, user_input):
        """Takes in user's input and decides what course of action the program should take: find book, add book to reading list, view reading list."""
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

    
    def parse_find_books_arg(self, args_list):
        """Formats query so that it can be read by Google Book's API."""
        if len(args_list) == 0:
            raise IndexError("Your search query must contain characters. Insert them after the '-f' flag.")

        return "+".join(args_list)