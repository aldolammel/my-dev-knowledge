#### Database > Tools > ERD > Relationship types
# Many-to-Many
---

**Before:**
1. [What is ERD and its basic](/database/_tools/ERD/_about.md)

---

Shorthand: `M:N`

This is the most flexible relationship type. There is zero, one, or many records on one side of the relationship, and zero, one, or many on the other. 

---
### Wrong usage
Applying *Many-To-Many* directly:

![](database/_tools/ERD/imgs/erd_many-to-many-wrong.png)

It's impossible to store multiple `author` IDs in just one `book` table's row on the db. That's why a *Map Table* is needed.

==Crucial!==
When two tables have a *Many-to-Many* relationship, this relation demands a *Map Table* (also known as *Junction Table* and *Bridge Table*) in between!
Once it's impossible to manage precisely data directly in *Many-To-Many* relations, *Map Table* is an intermediate table that forces original tables to use other type of relation more precise between them.

### Right usage
Creating the bridge in between:

![](database/_tools/ERD/imgs/erd_many-to-many.png)

**Notice:**
- The book was written by `one or many` authors.
- The author writes `none or many` books.
- Once `map_book_author` (*Map Table*) exists in between, both original tables only preserve their relationship with the opposite table;
- *Map Table* always tied itself to original tables using a [One-to-Many](database/_tools/ERD/one-to-many.md) relation;
- *Map Table* is a good opportunity to use *Composite Key* to build its Primary Key based on both original tables' PK.
- The "many" (Crow's foot symbol) side always requires to be connected directly in a FK (commonly something like `something_id`).
- Cardinality descriptions always are from the PK perspective to the FK (map table), e.g., "Book written by author" and "Author writes the book".

---
## Logic behind the mapping table creation:

![](database/_tools/ERD/imgs/erd_many-to-many_juction-eg1-1.png)
![](database/_tools/ERD/imgs/erd_many-to-many_juction-eg1-2.png)
![](database/_tools/ERD/imgs/erd_many-to-many_juction-eg1-3.png)
## Convention name well-acceptable:
I like to use `map_` for this extra table that *Many-to-Many* relationships demand, but by convention here you see other options for a prefix of table's name:

- Junction
- Mapping
- Cross-reference
- Join
- Bridge

---
## Other examples of many-to-many:

- A book can be associated with many categories. Each category is tied to many other books.
- The members of a family can own many pets.
- Recipes have multiple ingredients, and an ingredient can be used in many recipes.
- A doctor has many patients, and some patients see multiple doctors.