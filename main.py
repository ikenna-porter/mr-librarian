from src.reading_list import ReadingList
from src.argument_parser import ArgumentParser
from tabulate import tabulate
import queries

def main():
    arguments_parser = ArgumentParser()
    
    # Parses user input for command line argument and determines what command to execute based on provided argument
    user_input = arguments_parser.argument_parser_configs()
    argument = arguments_parser.parse_arguments(user_input)


    # If user does not provide argument 
    if argument == None:
        print(
            """\nYou must provide an argument. There are three options:
            \n* python main.py find-book -f <search query>\n* python main.py reading-list -a <1-5>\n* python main.py reading-list -v
            \nPlease choose one and proceed. For further assistance run the command 'python main.py --help'.\n"""
            )

    # If user entered 'find-book -f' argument (to search for a book from Google Books API):
    elif argument[0] == "f":
        print("\n", tabulate(argument[1], headers="keys", tablefmt="simple"), "\n") #displays fetched books

        if queries.does_fetched_books_table_exist() == 0:
            queries.create_and_insert_in_recently_fetched_table(argument[1])
        else:
            queries.delete_recently_fetched_books()
            queries.create_and_insert_in_recently_fetched_table(argument[1])

    # If user entered 'reading-list -a' argument (to add a book to reading list):
    elif argument[0] == "a":
        print(argument)
        list_ = ReadingList()
        list_.add_book(argument[1])
    
    # If user entered 'reading-list -v' argument (to view reading list):
    elif argument[0] == "v": 
        list_ = ReadingList()
        list_.view_list()



if __name__ == "__main__":
    main()