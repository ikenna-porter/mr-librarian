# Mr. Librarian

# Set Up
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

# Terminal Commands for Using App
1. All commands must be executed from the src directory
2. To find a book (using Google Books API):
```python main.py find-book -f <user input>```
4. To add a book to your book list:
```#python main.py book-list --add <number from 1 to 5>``
6. To view your book list:
```python main.py book-list --view```

# Running Unit Tests:
To run the unit tests, make sure you're in the application's root directory and run `python -m unittest`
