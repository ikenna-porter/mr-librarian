# Mr. Librarian

## Set Up
1. To set up the project on your local machine, fork the repo and clone it.
2. Create a virtual environment `python -m venv .venv`
3. Now activate it:
```
source .venv/bin/activate  #macOs
./.venv/Scripts/Activate.ps1 #windows
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

## Running Unit Tests:
To run the unit tests, make sure you're in the application's root directory and run `python -m unittest`.
This will run all the unit tests at once. To run them on a file-by-file basis, cd to the tests directory and run them using `python -m unittest <file-name>`

