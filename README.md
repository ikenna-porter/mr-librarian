# Mr. Librarian

## Set Up
1. To set up the project on your local machine, fork the repo and clone it.
2. Create a virtual environment with the following command:
```
source .venv/bin/activate  #macOs
./.venv/Scripts/Activate.ps1 #windows
```
3. Update pip `python -m pip install --upgrade pip`
4. Install all the dependencies in the requirements.txt file `pip install -r requirements.txt`
5. Create a new requirements.txt file from the installed pip packages `pip freeze > requirements.txt`
6. You can now use the app

## Terminal Commands for Using App
All commands must be executed from the root directory:
1. To find a book (using Google Books API):
```python main.py find-book -f <user input>```
2. To add a book to your book list:
```#python main.py book-list --add <number from 1 to 5>```
3. To view your book list:
```python main.py book-list --view```

## Running Unit Tests:
To run the unit tests, make sure you're in the application's root directory and run `python -m unittest`.
This will run all the unit tests at once. To run them on a file-by-file basis, cd to the tests directory and run them using `python -m unittest <directory-name>`

