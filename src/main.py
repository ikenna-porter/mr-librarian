from prompts import PromptManager
from api_manager import APIManager
from argument_parser import ArgumentParser

def main():

    PromptManager.print_welcome_text()
    user_input = ArgumentParser.argument_parser_configs()

    #takes user input and decides what to do with it
    arguments = ArgumentParser()
    response = arguments.parse_arguments(user_input)
    
    PromptManager.display_fetched_books(response)



if __name__ == "__main__":
    main()