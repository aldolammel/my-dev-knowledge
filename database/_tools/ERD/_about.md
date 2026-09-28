#### Database > Tools
# Entity-Relationship Diagram (ERD)

---

It's a visual representation of the logical structure of a database. It maps out how different pieces of information, called _entities_, relate to one another.

---
## Why use ERDs?

- **Database Design:** Acts as a blueprint before writing SQL or creating tables.
- **Visualization:** Helps developers, stakeholders, and database administrators understand complex data models at a glance.
- **Documentation:** Serves as a reference for how data flows and connects within an application.

---
## *Crow's Foot notation* pattern (recommended):

![](database/_tools/ERD/imgs/erd_general_example.png)

**Reading the ERD above:**
- A doctor treats `none or many` patients.
- A doctor attends `none or many` appointments.
- A patient has `one or many` appointments.
- A ward (small sector of a hospital) cares n`one or many` patients.
- A ward admits `none or many` appointments.

---
## Structure:

![](database/_tools/ERD/imgs/erd_structure.png)

- **Entity:** 
	- Object or concept that store data (e.g., `User`, `Product`, `Order`).
	- Represented by rectangles.
- **Attribute:**
	- The property or characteristic of an entity (e.g., a `User` entity has attributes like `email`, `username`, and `created_at`).
	- Represented by listed inside the entity box.
- **Cardinality/Relationship:**
	- How entity interact or connect with one another (e.g., a `User` places an `Order`).
	- Represented by connecting lines with cardinality markers (like [One-to-One](/database/_tools/ERD/one-to-one.md), [One-to-Many](/database/_tools/ERD/one-to-many.md), or [Many-to-Many](/database/_tools/ERD/many-to-many.md)).
	- The word "cardinality" in the image can be replaced by a small description about the relation between the tables's ID with the other table's FK.

---
## Relationship types:

- [One-to-One](/database/_tools/ERD/one-to-one.md)
- [One-to-Many](/database/_tools/ERD/one-to-many.md)
- [Many-to-Many](/database/_tools/ERD/many-to-many.md)
- [Self-referential](/database/_tools/ERD/self-referential.md)
- [Supertype/Subtype (inheritance)](/database/_tools/ERD/inheritance.md)

---
## Relationship cardinalities:

### Without business rule (don't use this shit)
![](database/_tools/ERD/imgs/relationship-cardinality.png)

- **Vertical line** ............................ can have only one related instance.
- **Crow's foot** ............................. can have many related instance.

### With business rule (RECOMMENDED)
![](database/_tools/ERD/imgs/relationship-cardinality-with-business-rule.png)

- **Duo vertical line** ............................ must have exactly one related instance - mandatory.
- **Circle + Vertical line** ..................... may have zero or max of one related instance.
- **Vertical line + Crow's foot**  ......... must have one or more related instances.
- **Circle + Crow's foot** ...................... may have zero or more related instances.

Text version of *Crow's Foot Notation* (read those 'single vertical lines as duo ones):
![](database/_tools/ERD/imgs/relationship-in-text.png)

---

## Business rules:
When your ERD also describe the business rule of each relationship, your document is much more powerful for the project planing.

![](database/_tools/ERD/imgs/erd_business-rule.png)


---

## Creating an ERD (roadmap):
[/database/\_tools/ERD/\_creating-a-erd](/database/_tools/ERD/_creating-a-erd.md)

## Generating/Exporting ERD from Django projects:
[/python/web-development/django/3-1-models-database/5-ERD/1-exporting-directly-from-django](/python/web-development/django/3-1-models-database/5-ERD/1-exporting-directly-from-django.md)
