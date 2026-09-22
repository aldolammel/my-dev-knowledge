#### Database > Tools
# Entity-Relationship Diagram (ERD)

---

It's a visual representation of the logical structure of a database. It maps out how different pieces of information, called _entities_, relate to one another.

## Crow's Foot notation pattern (recommended):

![](database/_tools/ERD/imgs/erd_with_crows-foot-notation.png)
![](database/_tools/ERD/imgs/erd_example.jpeg)
## Key components of an ERD include:

- **Entities:** Objects or concepts that store data (e.g., `User`, `Product`, `Order`). Represented by rectangles.
- **Attributes:** The properties or characteristics of an entity (e.g., a `User` entity has attributes like `email`, `username`, and `created_at`). Represented by ovals or listed inside the entity box.
- **Relationships:** How entities interact or connect with one another (e.g., a `User` places an `Order`). Represented by connecting lines with cardinality markers (like one-to-one, one-to-many, or many-to-many).
### Why use ERDs?

- **Database Design:** Acts as a blueprint before writing SQL or creating tables.
- **Visualization:** Helps developers, stakeholders, and database administrators understand complex data models at a glance.
- **Documentation:** Serves as a reference for how data flows and connects within an application.

---
## Relationship types:
[/database/\_basic-concepts/relationship-types/\_types](database/_basic-concepts/relationship-types.md)

---
## Relationship cardinality:

![](database/_tools/ERD/imgs/relationship-cardinality.png)

- **line** = one;
- **crow's foot** = many or infinite;
- **line + line** = one and only one (mandatory);
- **circle + line** = zero to a maximum of one;
- **line + crow's foot** = a minimum of one to many;
- **circle + crow's foot** = zero to many;

==Important==
You can add a text in the relationship line to indicate what relation is that between tables like "has", "belongs", "attends", "cares", etc... Check the hospital example below.

**The same but using text:**
- `1:N` or `1:*` means `None, one or many (one-to-many)`;
- `N:M` or `*:*` means `Many-to-many (requires a junction/intermediate table)`;
- `1:1` means `One and only one (strict one-to-one relationship)`; 

---
## Hospital management example:

![](database/_tools/ERD/imgs/erd_hospital-management.png)

**Translating the ERD above:**
- Patient is treated by `one and only one` doctor; 
- Patient has `at least one or many` appointments;
- Patient is cared by `one and only one` hospital ward; 
- Doctor treats `none, one or many` patients; 
- Doctor attends `none, one, or many` appointments; 
- Appointment is attended by `one and only one` doctor; 
- Appointment has `one and only one` patient; 
- Appointment is admitted by `one and only one` ward;
- Ward cares `none, one or many` patients; 
- Ward cares `none, one or many` appointments; 

---
## Generating/Exporting ERD from Django projects:
[/python/web-development/django/3-1-models-database/5-ERD/1-exporting-directly-from-django](/python/web-development/django/3-1-models-database/5-ERD/1-exporting-directly-from-django.md)
