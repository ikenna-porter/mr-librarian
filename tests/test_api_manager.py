import unittest
from unittest.mock import patch, MagicMock
import json
from src.api_manager import APIManager


class TestAPIManager(unittest.TestCase):

    def setUp(self):
        self.test_object_1 = APIManager()

    @patch("src.api_manager.requests")
    def test_fetch_books(self, mock_requests):

        with open("./tests/testing_data_1.json") as file:
            json_data = json.load(file)

        result = [{'id': 1, 'title': "Harry Potter and the philosopher's stone", 'authors': 'J. K. Rowling', 'publisher': 'N/A'}, {'id': 2, 'title': 'Harry Potter y la piedra filosofal', 'authors': 'J.K. Rowling', 'publisher': 'Pottermore Publishing'}, {'id': 3, 'title': 'Harry Potter y la Orden del Fénix (20 Aniv. Gryffindor) / Harry Potter and the O rder of the Phoenix (Gryffindor)', 'authors': 'J. K. Rowling', 'publisher': 'National Geographic Books'}, {'id': 4, 'title': "Harry Potter y la piedra filosofal. Edición ilustrada / Harry Potter and the Sorcerer's Stone: The Illustrated Edition", 'authors': 'J.K. Rowling', 'publisher': 'National Geographic Books'}, {'id': 5, 'title': 'Harry Potter y la cámara secreta', 'authors': 'J. K. Rowling', 'publisher': 'Emece'}]

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = json_data
        mock_requests.get.return_value = mock_response
        user_input = "harry+potter"

        self.assertEqual(self.test_object_1.fetch_books(user_input), result)

    def test_clean_data(self):
        with open("./tests/testing_data_2.json") as file:
            data = json.load(file)
        
        test = self.test_object_1.clean_up_data(data)

        cleaned_data = [
            {'id': 1, 'title': 'Caring for Cut Flowers', 'authors': 'Rod Jones', 'publisher': 'Landlinks Press'},
            {'id': 2, 'title': 'Bead Flowers', 'authors': 'Minako Shimonagase', 'publisher': 'Japan Publications Trading'},
            {'id': 3, 'title': 'Flowers Chronicles', 'authors': 'Pugh Brown Flowers', 'publisher': 'N/A'},
            {'id': 4, 'title': 'Flowers In The Attic', 'authors': 'V.C. Andrews', 'publisher': 'Simon and Schuster'},
            {'id': 5, 'title': 'Flowers and Nature', 'authors': 'Sam Segal', 'publisher': 'Seven Hills Books'},
        ]
        self.assertEquals(test, cleaned_data)
    
        

if __name__ == '__main__':
    unittest.main()
