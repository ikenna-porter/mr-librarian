from src.prompts import PromptManager
from src.api_manager import APIManager
from src.reading_list import ReadingList
from src.argument_parser import ArgumentParser
import queries


def main():
    prompt = PromptManager()
    prompt.print_welcome_text()


    user_input = ArgumentParser.argument_parser_configs()

    #parses user input to determine what command to execute
    arguments = ArgumentParser()
    response = arguments.parse_arguments(user_input)

    #if user chose to find a book from API
    if response[0] == "f":
        prompt.display_fetched_books(response[1])

        if queries.does_fetched_books_table_exist() == 0:
            print(queries.does_fetched_books_table_exist())
            queries.create_and_insert_in_recently_fetched_table(response[1])
        else:
            print(queries.does_fetched_books_table_exist())
            queries.delete_recently_fetched_books()
            queries.create_and_insert_in_recently_fetched_table(response[1])

    #if user chose to add a book to reading list
    elif response[0] == "a":
        list_ = ReadingList()
        list_.add_book(response[1])
    
    #if user chose to view reading list
    elif response[0] == "v": 
        list_ = ReadingList()
        list_.view_list()



if __name__ == "__main__":
    main()