"""
DATABASE: SIMPLEST SOLUTION WITH SQL

"""

import sqlite3

db = sqlite3.connect("database.db")  # If no db file, it will create the file.

cursor = db.cursor()  # it's the mouse that will execute each given command.

cursor.execute(
    "CREATE TABLE books ("
    "id INTEGER PRIMARY KEY, "
    "title varchar(250) NOT NULL UNIQUE, "
    "author varchar(250) NOT NULL, "
    "rating FLOAT NOT NULL"
    ")")

cursor.execute("INSERT INTO books VALUES("
               "1, "
               "'Harry Potter', "
               "'J. K. Rowling', "
               "'9.3'"
               ")")

db.commit()
