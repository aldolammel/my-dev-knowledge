#### Database > Tools > ERD > Relationship types
# One-to-Many / Many-to-One
---

**Before:**
1. [What is ERD and its basic](/database/_tools/ERD/_about.md)

---

Shorthand: `1:N`

This is the most common relationship type. In this relationship, there is one record on one side of the relationship, and zero, one, or many on the other. From the linked table, the one-to-many relationship becomes a many-to-one relationship. For example, a biological mom can have many children, but each child can only have one biological mom.

![](database/_tools/ERD/imgs/erd_one-to-many.png)

**Notice:**
- The publisher publishes `none or many` books.
- The "many" (Crow's foot symbol) side always requires to be connected directly in a FK (commonly something like `something_id`).
- Cardinality descriptions always are from the PK perspective to the FK, e.g., "Publisher publishes the book".

## Other examples of one-to-many:

- One book can have more than one author. For example, the 1996 book _Tube: The Invention of Television_ was written by David E. Fisher and Marshall Jon Fisher. 
- A city can have many ZIP codes.
- A state can have multiple area codes. 
- A state can have many cities.
- A customer can make many orders from a vendor, and each order can have multiple products.
- One student can be registered in many classes.
- An album (usually) contains many songs.