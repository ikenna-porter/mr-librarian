import argparse
from tabulate import tabulate
class PromptManager():

    def print_welcome_text():
        print("Hello there! Welcome to Mr. Librarian.\nType 'python main.py --help' for guidance.\n")

    def display_fetched_books(books):
        print(tabulate(books, headers="keys", tablefmt="simple"))

    def print_book_list():
        pass
