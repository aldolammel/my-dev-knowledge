#### Database > Basic concepts > Relationship types
# Self-Referential / Recursive
---

A self-referential (also known as recursive) relationship is one that links to another row in the same table. This is used for specific situations, for example, if you have a table for users and the user can have a boss. This boss would be another user, so the attribute (e.g.) `report_to_id` would be another row in the same table.

![](database/_basic-concepts/relationship-types/imgs/erd_self-referential.png)

**Reading this cardinality:**
- The current user is managed by nobody or someone.
- And if there is a manager, that manager (id) could manage nobody or many people.

==Important:==
The attribute/field that will refer to the same table is always a foreignkey not differing from other relations simply because it points to the same table.