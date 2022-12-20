from prompts import PromptManager
from api_manager import APIManager
from argument_parser import ArgumentParser

def main():
    prompt = PromptManager()
    prompt.print_welcome_text()

    #assigns None to current_books if there is no value. Otherwise value remains the same
    # current_books if current_books else None
    user_input = ArgumentParser.argument_parser_configs()

    #takes user input and decides what to do with it
    arguments = ArgumentParser()
    response = arguments.parse_arguments(user_input)
    if response[0] == "f":
        current_books = response[1]
        prompt.display_fetched_books(response)
    # elif response[0] == "v":
    #     print(current_books)
    #     print("v")



if __name__ == "__main__":
    main()