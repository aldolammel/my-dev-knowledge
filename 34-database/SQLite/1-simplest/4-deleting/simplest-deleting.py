"""
PERSISTENT DATA: SQLITE

    + How to delete a specific entry;
    + How to delete all entries from a specific table;

"""
import sqlite3


def delete_by_id(mov_id):
    # Use a context manager to ensure the connection is properly closed:
    with sqlite3.connect("database.db") as db:
        # Creating the cursor that will interact with the database:
        cursor = db.cursor()
        try:
            # Deleting the specific entry from 'movies' table:
            cursor.execute("DELETE FROM movies WHERE id = ?", (mov_id,))
            # Commit the changes and close the connection:
            db.commit()
            if cursor.rowcount == 0:
                print(f"No movie found with ID {mov_id}.\n")
            else:
                print(f"Movie with ID {mov_id} deleted.\n")
        except sqlite3.Error as error:
            print(f"SQLite >> An error occurred: {error}")
        finally:
            # It's generally good practice to close the cursor when done:
            cursor.close()


def delete_all():
    # Use a context manager to ensure the connection is properly closed:
    with sqlite3.connect("database.db") as db:
        # Creating the cursor that will interact with the database:
        cursor = db.cursor()
        try:
            # Deleting all entries in 'movies' table:
            cursor.execute("DELETE FROM movies")
            # Commit the changes and close the connection:
            db.commit()
            print("All movies deleted.\n")
        except sqlite3.Error as error:
            print(f"SQLite >> An error occurred: {error}")
        finally:
            # It's generally good practice to close the cursor when done:
            cursor.close()


# TO TEST --------------------------------
delete_by_id(1)
# delete_all()
