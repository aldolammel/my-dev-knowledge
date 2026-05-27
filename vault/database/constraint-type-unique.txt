

DATABASE CONSTRAINTS: UNIQUE

    Ensures all values in a column (or combination of columns) are unique.

    E.g
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE
        );
