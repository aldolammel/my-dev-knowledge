#### Database > Basic concepts > Relationship types
# Many-to-Many
---

This is the most flexible relationship type. There is zero, one, or many records on one side of the relationship, and zero, one, or many on the other. 

![](database/_basic-concepts/relationship-types/imgs/erd_many-to-many.png)

## Many-to-Many tables requires an intermediate one:

Many-to-many relationships require an intermediate table to make the connection, because relational systems can’t directly manage the connection. These tables have many names (by convention), including:

- Junction
- Linking
- Cross-reference
- Mapping
- Join
- Associative

E.g.
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