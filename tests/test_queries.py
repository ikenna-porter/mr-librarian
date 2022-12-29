
import os
import unittest
from unittest.mock import patch, MagicMock, Mock
import sqlite3
import queries

class TestMockDatabase(unittest.TestCase):

    def setUp(self):
        """
        Setup a temporary database
        """
        conn = sqlite3.connect("mock.db")
        cursor = conn.cursor()

        # create a table
        cursor.execute("""
            CREATE TABLE mock_reading_list (
                title text,
                author text,
                publisher text
        )""")

        # insert multiple records
        books = [
            {"title":"Pride and Prejudice", "authors":"Jane Austen", "publisher": "Whitehall"},
            {"title":"The Red and the Black", "authors":"Stendhal", "publisher": "A. Levasseur"},
            {"title":"War and Peace", "authors":"Tolstoy", "publisher": "The Russian Messenger"},
            {"title":"Wuthering Heights", "authors":"Emily Bronte", "publisher": "Thomas Cautley Newby"},
            {"title":"Le Pere Goriot", "authors":"Honore de Balzac", "publisher": "Revue de Paris"},
        ]
        cursor.executemany("INSERT INTO mock_reading_list VALUES (?,?,?)", (books[1], books[2], books[3]))

        # save data to database
        conn.commit()

    def tearDown(self):
        """
        Delete the database
        """
        os.remove("mock.db")
    
    def test_select_reading_list(self):
        actual = queries.select_reading_list()
        expected = self.books
        print(actual)

