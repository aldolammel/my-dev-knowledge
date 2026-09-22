#### Database > Basic concepts > Relationship types
# Many-to-Many
---

Shorthand: `M:N`

This is the most flexible relationship type. There is zero, one, or many records on one side of the relationship, and zero, one, or many on the other. 

==Crucial!==
*Many-to-Many* tables require an intermediate one!

Many-to-many relationships require an intermediate table to make the connection, because relational systems can’t directly manage the connection. 

**Wrong usage:**
![](database/_basic-concepts/relationship-types/imgs/erd_many-to-many_wrong.png)

It's impossible to store multiple author IDs in just one Book row on the db. That's why an intermediate table is needed.

**Right usage:**
![](database/_basic-concepts/relationship-types/imgs/erd_many-to-many_right.png)

Notice:
- Once `map_book_author` exists in between, both original tables preserve their original relationship with the `map_book_author` table, but the `map_book_author` uses a [One-to-Many](/database/_basic-concepts/relationship-types/one-to-many.md), making the relation be much more specific between the data.
- `map_book_author` table is using a composite key built-up by both Primary Keys that compose the mapping table.

---
## Convention name:
This "extra" table that *Many-to-Many* relationships demand has, by convention, some options for its prefix name:

- Mapping
- Junction
- Cross-reference
- Join

---
## Logic behind the mapping table creation:

![](database/_basic-concepts/relationship-types/imgs/erd_many-to-many_juction-eg1-1.png)
![](database/_basic-concepts/relationship-types/imgs/erd_many-to-many_juction-eg1-2.png)
![](database/_basic-concepts/relationship-types/imgs/erd_many-to-many_juction-eg1-3.png)
## Other examples of many-to-many:

- A book can be associated with many categories. For example, _Dia 922, Uma longa história sobre estrada_, a 2021 book by Aldo Lammel (me), is linked to different shelf categories: Road diaries, Portuguese literature, Non-fictional. Each of those categories are linked to many other books.
- The members of a family can own many pets.
- Recipes have multiple ingredients, and an ingredient can be used in many recipes.
- A doctor has many patients, and some patients see multiple doctors.
- A worker can be responsible for many tasks, and each task can be handled by many workers.
- Many customers can buy multiple products.
- Each class has multiple students; each teacher teaches multiple classes.
- A salesperson can have many clients, and each client might have many salespeople (especially if they are larger clients). 
- A Twitter user probably is followed by many people and follows many others; those two groups won’t necessarily match.