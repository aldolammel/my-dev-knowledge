#### Database > Tools > ERD > Relationship types
# Self-Referential / Recursive
---

**Before:**
1. [What is ERD and its basic](/database/_tools/ERD/_about.md)

---

A self-referential (also known as recursive) relationship is one that links to another row in the same table. This is used for specific situations, for example, if you have a table for users and the user can have a boss. This boss would be another user, so the attribute (e.g.) `report_to_id` would be another row in the same table.

![](database/_tools/ERD/imgs/erd_self-referential.png)

**Notice:**
- The user manages `none or one` user.
- The current user is managed by nobody or someone.
- And if there is a manager, that manager (id) could manage nobody or many people.
- The "many" (Crow's foot symbol) side always requires to be connected directly in a FK (commonly something like `something_id`).
- Cardinality descriptions always are from the PK perspective to the FK, e.g., "User (id) manages other user (report_to_id)".

==Important:==
The attribute/field that will refer to the same table is always a foreignkey not differing from other relations simply because it points to the same table.

## Is it possible a Self-Referential relationship be many-to-many?
I don't think so!

