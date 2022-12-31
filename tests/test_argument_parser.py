import unittest
from unittest.mock import patch
from src.argument_parser import ArgumentParser


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TestArgumentParser(unittest.TestCase):

    def setUp(self):
        self.test_object_1 = ArgumentParser()
        self.test_object_2 = ArgumentParser()
        self.test_object_3 = ArgumentParser()
        self.books = [
            {'id': 1, 'title': 'War in Heaven', 'authors': 'Helen Caldicott, Craig R. Eisendrath', 'publisher': 'N/A'},
            {'id': 2, 'title': "Heaven's Promise", 'authors': 'Rachel Wilson', 'publisher': 'Berkley'},
            {'id': 3, 'title': "Heaven's Fury", 'authors': 'Meta Smith, 50 Cent', 'publisher': 'Simon and Schuster'},
            {'id': 4, 'title': 'Heaven and its Wonders, and Hell. ... Originally published in Latin at London, A.D. 1758', 'authors': 'Emanuel Swedenborg', 'publisher': 'N/A'},
            {'id': 5, 'title': "Heaven's Luck", 'authors': 'harold hester', 'publisher': 'Lulu.com'},
        ]

    
    # def test_argument_parser_configs(self):
        # This method is basically a wrapper function for the argparse library. 
        # It does not take any input and the output varies depending on what the argparse library return.
        # Because of this, I assume it cannot be tested?
        # pass

    
    def test_parse_find_books_arg(self):
        # Note: argparse library automatically converts all data type into strings, so there is no need to test for ints
        test_1 = self.test_object_1.parse_find_books_arg(["1", "2", "3"])
        # Tests for no input:
        test_2 = self.test_object_2.parse_find_books_arg
        test_3 = self.test_object_3.parse_find_books_arg(["clean", "code"])

        self.assertEqual(test_1, "1+2+3")
        self.assertRaises(IndexError, test_2, [])
        self.assertEqual(test_3, "clean+code")
    
    @patch("src.api_manager.APIManager.fetch_books")
    def test_parse_arguments(self, mock_fetch_books):
        user_input_1 = Namespace(a='1', v=False)
        user_input_2 = Namespace(a=None, v=True)
        user_input_3 = Namespace(f=['heaven'])
        mock_fetch_books.return_value = self.books

        test_1 = self.test_object_1.parse_arguments(user_input_1)
        test_2 = self.test_object_2.parse_arguments(user_input_2)
        test_3 = self.test_object_3.parse_arguments(user_input_3)

        self.assertEqual(test_1, ["a", "1"])
        self.assertEqual(test_2, ["v"])
        self.assertEqual(test_3, ["f", self.books])


if __name__ == '__main__':
    unittest.main()
