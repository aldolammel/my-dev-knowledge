#### Database > Basic concepts
# Relationship types

---

Relationships are the cornerstone of relational databases. Users can query the database and get results that combine data from different tables into a single table. For example, if you own a record store, the database might have a table for albums, another for song titles, and another for artists.

To better visualize these relationships, check how we draw it in a *ER diagram*: [/database/_tools/ERD/_about](/database/_tools/ERD/_about.md)

---
## Type > One-to-One
There is one and only one record on each side of the relationship. Each row in a table is connected to a single row in another table.

[one-to-many](/database/_tools/ERD/one-to-many.md)

---
## Type > One-to-Many
There is one record on one side of the relationship, and zero, one, or many on the other.

[one-to-many](/database/_tools/ERD/one-to-many.md)

---
## Type > Many-to-Many
There is zero, one, or many records on one side of the relationship, and zero, one, or many on the other.

[many-to-many](/database/_tools/ERD/many-to-many.md)

---
## Type > Self-Referential
A self-referential relationship is one that links to another row in the same table.

[self-referential](/database/_tools/ERD/self-referential.md)

---
## Type > Supertype/Subtype (inheritance)
How to represent when an entity inherits attributes from another entity

[inheritance](/database/_tools/ERD/inheritance.md)

---
## Entity-Relationship Diagram (ERD)
[/database/\_tools/ERD/\_about](database/_tools/ERD/_about.md)
## Cardinality between Parent and Child classes:
[inheritance](/database/_tools/ERD/inheritance.md)
