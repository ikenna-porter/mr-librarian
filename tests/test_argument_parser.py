import unittest
# from src.api_manager import APIManager
from src.argument_parser import ArgumentParser


class TestArgumentParser(unittest.TestCase):

    def setUp(self):
        self.test_object_1 = ArgumentParser()
        self.test_object_2 = ArgumentParser()
        self.test_object_3 = ArgumentParser()

    # def test_parse_arguments(self):
    #     query = self.test_object_1.parse_find_books_arg(["harry"])
    #     fetch_data = APIManager()
        
    #     self.assertEquals(fetch_data.fetch_books(query))
    
    def test_parse_find_books_arg(self):

        #Note: argparse library automatically converts all data type into strings, so there is no need to test for ints
        test_1 = self.test_object_1.parse_find_books_arg(["1", "2", "3"])

        #tests for no input:
        test_2 = self.test_object_2.parse_find_books_arg
        test_3 = self.test_object_3.parse_find_books_arg(["clean", "code"])

        self.assertEquals(test_1, "1+2+3")
        self.assertRaises(IndexError, test_2, [])
        self.assertEquals(test_3, "clean+code")


if __name__ == '__main__':
    unittest.main()
