import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("PROJECT_API_KEY")

class APIManager():
    """A class responsible for fetching, decoding and changing the shape of data received from Google Books API"""
    
    def fetch_books(self, user_input):
        """Fetches 5 books that match the users query and removed unnecessary data"""

        url = f"https://www.googleapis.com/books/v1/volumes?q={user_input}&maxResults=5&key={API_KEY}"
        response = requests.get(url)
        retrieved_books = response.json()
        return self.clean_up_data(retrieved_books)

    def clean_up_data(self, books):
        """Removes unnecessary book dat from response body"""
        filtered_books = []
        book_id = 1

        for book in books["items"]:
            necessary_book_data = {}
            necessary_book_data["id"] = book_id
            book_id+=1
            necessary_book_data["title"] = book["volumeInfo"]["title"]
            necessary_book_data["authors"] = ", ".join(book["volumeInfo"]["authors"])
            publisher = book["volumeInfo"].get("publisher")
            necessary_book_data["publisher"] = publisher if publisher else "N/A"
            filtered_books.append(necessary_book_data)

        return filtered_books

