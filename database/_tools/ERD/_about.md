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

![](database/_tools/ERD/imgs/erd_hospital-management.png)

**Reading the ERD above:**
- Patient is treated by `one and only one` doctor.
- Patient has `at least one or many` appointments.
- Patient is cared by `one and only one` hospital ward.
- Doctor treats `none, one or many` patients.
- Doctor attends `none, one, or many` appointments.
- Appointment is attended by `one and only one` doctor.
- Appointment has `one and only one` patient.
- Appointment is admitted by `one and only one` ward.
- Ward cares `none, one or many` patients.
- Ward cares `none, one or many` appointments.
- (Optional) You can add a text in the cardinality line to indicate what kind of relation is that.

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
	- Represented by connecting lines with cardinality markers (like [One-to-One](/database/\_basic-concepts/relationship-types/one-to-one.md), [One-to-Many](/database/\_basic-concepts/relationship-types/one-to-many.md), or [Many-to-Many](/database/\_basic-concepts/relationship-types/many-to-many.md)).

---
## Relationship types:

- One-to-One
- One-to-Many
- Many-to-Many
- Self-referential

[/database/\_basic-concepts/relationship-types/\_types](database/_basic-concepts/relationship-types.md)

---
## Relationship cardinalities:

### Without business rule
![](database/_tools/ERD/imgs/relationship-cardinality.png)
### With business rule
==RECOMMENDED!==
![](database/_tools/ERD/imgs/relationship-cardinality-with-business-rule.png)

- **Duo vertical line** ............................ must have exactly one related instance - mandatory.
- **Circle + Vertical line** ..................... may have zero or max of one related instance.
- **Vertical line + Crow's foot**  ......... must have one or more related instances.
- **Circle + Crow's foot** ...................... may have zero or more related instances.

Text version of *Crow's Foot Notation*:
![](database/_tools/ERD/imgs/relationship-in-text.png)

---

## Business rules:
When your ERD also describe the business rule of each relationship, your document is much more powerful for the project planing.

![](database/_tools/ERD/imgs/erd_business-rule.png)


---
## Generating/Exporting ERD from Django projects:
[/python/web-development/django/3-1-models-database/5-ERD/1-exporting-directly-from-django](/python/web-development/django/3-1-models-database/5-ERD/1-exporting-directly-from-django.md)
