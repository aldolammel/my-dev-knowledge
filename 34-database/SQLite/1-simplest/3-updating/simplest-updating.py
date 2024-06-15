"""
PERSISTENT DATA: SQLITE

    + How to add a new entry (updating the db);


"""
import sqlite3


def add_movie(id_, title, director, rating, is_in_cinema):
    # Use a context manager to ensure the connection is properly closed:
    with sqlite3.connect("database.db") as db:
        # Creating the cursor that will interact with the database:
        cursor = db.cursor()
        try:
            # Adding the new data:
            cursor.execute(
                "INSERT INTO movies VALUES("
                f"{id_},"
                f"'{title}',"
                f"'{director}',"
                f"'{rating}',"
                f"{is_in_cinema}"
                ")"
            )
            # Commit the changes and close the connection:
            db.commit()

        except sqlite3.Error as error:
            print(f"SQLite >> An error occurred while adding a new movie: {error}")
        finally:
            # It's generally good practice to close the cursor when done:
            cursor.close()


# ----------------------------------------------------------------------------------------------------------------------
#    TO TEST:
#    1) Open the db and check the current entries.
#    2) Edit the information below with a new entry data, mainly the id.

add_movie(id_=3, title="New Title", director="Vini Azevedo", rating=5.9, is_in_cinema=1)
