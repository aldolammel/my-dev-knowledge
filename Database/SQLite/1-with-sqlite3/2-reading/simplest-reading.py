"""
PERSISTENT DATA: DATABASE WITH SQLITE3: READING

    + How to read a specific entry;
    + How to read all entries from a specific table;

"""
import sqlite3


def find_by_id(entry_id):
    # Use a context manager to ensure the connection is properly closed:
    with sqlite3.connect("database.db") as db:
        # Creating the cursor that will interact with the database:
        cursor = db.cursor()
        try:
            # Selecting the specific entry from 'movies' table:
            cursor.execute("SELECT * FROM movies WHERE id = ?", (entry_id,))
            # Saves that selection:
            result = cursor.fetchone()
            if result:
                print(f"Movie with id {entry_id} is: {result}\n")
            else:
                print(f"No entry found with id {entry_id}.\n")
        except sqlite3.Error as error:
            print(f"SQLite >> An error occurred while querying the entry by id: {error}")
        finally:
            # It's generally good practice to close the cursor when done:
            cursor.close()


def find_all():
    # Use a context manager to ensure the connection is properly closed:
    with sqlite3.connect("database.db") as db:
        # Creating the cursor that will interact with the database:
        cursor = db.cursor()
        try:
            # Selecting all entries from 'movies' table:
            cursor.execute("SELECT * FROM movies")
            # Saves that selection:
            results = cursor.fetchall()
            if results:
                print("All entries in the 'movies' table:")
                for row in results:
                    print(row)
            else:
                print("No entries found in the 'movies' table.\n")
        except sqlite3.Error as error:
            print(f"SQLite >> An error occurred while querying all entries: {error}")
        finally:
            # It's generally good practice to close the cursor when done:
            cursor.close()


# Searching for movie with this ID:
find_by_id(2)

# Printing all movies out:
find_all()
