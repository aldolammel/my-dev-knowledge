"""
PERSISTENT DATA: DATABASE WITH SQLITE3: CREATING

    + How to create a database with tables:


"""
import sqlite3
# Use a context manager to ensure the connection is properly closed:
with sqlite3.connect("database.db") as db:
    # If no db file, it will create the file!
    # Creating the cursor that will interact with the database:
    cursor = db.cursor()
    try:
        # Create the 'movies' table:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            director TEXT NOT NULL,
            rating REAL NOT NULL,
            is_in_cinema INTEGER NOT NULL CHECK (is_in_cinema IN (0, 1))
        )
        """)
        # Commit the changes and close the connection:
        db.commit()

    except sqlite3.Error as error:
        print(f"SQLite >> An error occurred while creating the table: {error}")

    finally:
        # It's generally good practice to close the cursor when done:
        cursor.close()
