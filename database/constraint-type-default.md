

DATABASE CONSTRAINTS: DEFAULT

    Sets a default value if none is provided.

    E.g
        CREATE TABLE posts (
            id SERIAL PRIMARY KEY,
            views INT DEFAULT 0
        );
