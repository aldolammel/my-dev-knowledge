DATABASE: CONSTRAINTS

    A constraint in a database is a rule that restricts what kind of values can be stored in a column or across multiple columns.

    It’s the database’s way of saying: “I will only accept data that follows this rule, otherwise I reject it.”

    Constraints are essential because they:

    - Protect data integrity (no invalid/illogical data sneaks in)
    - Enforce business rules at the lowest level (DB, not just in your app)
    - Save you from bugs caused by bad data entered outside Django (via raw SQL, external tools, etc.)


    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    PRIMARY KEY:
        /database/constraint-type-primary-key.md

    FOREIGN KEY:
        /database/constraint-type-foreign-key.md

    NOT NULL:
        /database/constraint-type-not-null.md

    UNIQUE:
        /database/constraint-type-unique.md

    CHECK:
        /database/constraint-type-check.md

    DEFAULT:
        /database/constraint-type-default.md
