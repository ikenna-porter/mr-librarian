import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("PROJECT_API_KEY")

class APIManager():
    """A class responsible for fetching, decoding and changing the shape of data received from Google Books API"""
    
    def fetch_books(self, user_input):
        """A method that performs the fetch request"""

        url = f"https://www.googleapis.com/books/v1/volumes?q={user_input}key={API_KEY}"
        response = requests.get(url)
        print(response)
        print(response.json())


    def decode():
        pass

    def clean_up_data():
        pass