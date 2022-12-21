
# import os
# import unittest
# from unittest.mock import patch, MagicMock, Mock
# import sqlite3
# import queries

# class TestMockDatabase(unittest.TestCase):

#     def setUp(self):
#         """
#         Setup a temporary database
#         """
#         self.conn = sqlite3.connect("reading-list.db")
#         self.cursor = self.conn.cursor()

#         # create a table
#         self.cursor.execute("""
#             CREATE TABLE reading_list (
#                 title text,
#                 author text,
#                 publisher text
#         )""")

#         # insert multiple records
#         self.books = [
#             {"title":"Pride and Prejudice", "authors":"Jane Austen", "publisher": "Whitehall"},
#             {"title":"The Red and the Black", "authors":"Stendhal", "publisher": "A. Levasseur"},
#             {"title":"War and Peace", "authors":"Tolstoy", "publisher": "The Russian Messenger"},
#             {"title":"Wuthering Heights", "authors":"Emily Bronte", "publisher": "Thomas Cautley Newby"},
#             {"title":"Le Pere Goriot", "authors":"Honore de Balzac", "publisher": "Revue de Paris"},
#         ]
#         self.cursor.executemany("INSERT INTO reading_list VALUES (?,?,?)", (self.books[1], self.books[2], self.books[3]))

#         # save data to database
#         self.conn.commit()

#     def tearDown(self):
#         """
#         Delete the database
#         """
#         os.remove("reading-list.db")
    
#     def test_select_reading_list(self):
#         actual = queries.select_reading_list()
#         expected = self.books

