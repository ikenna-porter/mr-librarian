# Mr. Librarian

## Description
Mr. Librarian is a command-line book list app that allows users to search for books (using Google Books API) and store the results of the search query in their personal reading list.

## Installation
1. To set up the project on your machine, fork the repo and clone it.
2. Create a virtual environment `python -m venv .venv`
3. Now, activate it:
```
#macOs:
source .venv/bin/activate

#windows:
./.venv/Scripts/Activate.ps1 
```
4. Update pip `python -m pip install --upgrade pip`
5. Install all the dependencies in the requirements.txt file `pip install -r requirements.txt`
6. Create a new requirements.txt file from the installed pip packages `pip freeze > requirements.txt`
7. You can now use the app

## Terminal Commands for Using App
All commands must be executed from the root directory:

* ### Find book using Google Books API
```python main.py find-book -f <user input>```

* ### Add book to reading list
Using an ID from the previous command output, add a book to your reading list:
```python main.py reading-list -a <number from 1 to 5>```

* ### View reading list
```python main.py reading-list -v```

## Running Unit Tests
To run the unit tests, make sure you're in the application's root directory and run `python -m unittest`.
This will run all the unit tests at once. To run them on a file-by-file basis, cd to the tests directory and run them using `python -m unittest <file-name>`

## Known Bugs and Errors
Unfortunately, I was unable to add units tests for the queries.py and reading_list.py files since the methods in both files run SQL queries to interact with the database. The initial unit tests queried the database itself, which produced an unwanted side-effect.

## Future
Below are some features to improve the application in the future:
* Support all CRUD functionality for reading list - right now it cannot be completely updated (deleting books) and it cannot be deleted. 
* Implement the unittest.mock library so that database isn't directly queried while testing
