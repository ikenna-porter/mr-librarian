import os
import requests

# This code was originally used to keep API Key private. For the sake of having others use API, I've provided key below.
# from dotenv import load_dotenv
# load_dotenv()
# API_KEY = os.getenv("PROJECT_API_KEY")
API_KEY = "AIzaSyDsPduq9rw52gI2fD4YlH8vQhrne0Pkxv0"
API_KEY_2 = "AIzaSyA9WjhId1RoXb_UpxcKOz1yR3pwnVYhtBQ"

class APIManager():
    """A class responsible for fetching, decoding and changing the shape of data received from Google Books API."""
    
    def fetch_books(self, user_input):
        """Fetches 5 books that match the users query and removed unnecessary data."""

        url = f"https://www.googleapis.com/books/v1/volumes?q={user_input}&maxResults=5&key={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            retrieved_books = response.json()
            
            # Prints error message it a book matching query couldn't be found.
            if retrieved_books["totalItems"] == 0:
                print("\nWe couldn't find any books that match your query. Please submit a different query.\n")
                return

            return self.clean_up_data(retrieved_books)
        else:
            print("Error retrieving book data from API. Check logs for additional information.")

    def clean_up_data(self, books):
        """Removes unnecessary book data from response body."""
        filtered_books = []
        book_id = 1

        for book in books["items"]:
            necessary_book_data = {}
            necessary_book_data["id"] = book_id
            book_id+=1

            #handles edge case of no title
            title = book["volumeInfo"].get("title")
            necessary_book_data["title"] = title if title else "N/A"

            #handles edge case of no author
            authors = book["volumeInfo"].get("authors")
            necessary_book_data["authors"] = ", ".join(authors) if authors else "N/A"

            #handles edge case of no publisher
            publisher = book["volumeInfo"].get("publisher")
            necessary_book_data["publisher"] = publisher if publisher else "N/A"

            filtered_books.append(necessary_book_data)
        return filtered_books

