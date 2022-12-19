from prompts import PromptManager
from api_manager import APIManager
from argument_parser import ArgumentParser

def main():

    PromptManager.print_welcome_text()
    user_input = ArgumentParser.argument_parser_configs()

    arguments = ArgumentParser()
    arguments.parse_arguments(user_input)




if __name__ == "__main__":
    main()