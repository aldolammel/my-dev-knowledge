#### Database > Basic concepts > Relationship types
# Supertype/Subtype (inheritance)

---

In Crow's Foot (and ER modeling generally), when a child entity's PK is also the same attribute that's connected to the parent's PK, you're modeling a supertype/subtype relationship (specialization/generalization) that can be understood as inheritance.

---
## Cardinality between Parent and Child entities/tables:

![](database/_basic-concepts/relationship-types/imgs/erd_inherits.png)

**Notice:**
- To use the *Supertype/Subtype* benefits, the relationship type must be [one-to-one](/database/_basic-concepts/relationship-types/one-to-one.md) or [one-to-many](/database/_basic-concepts/relationship-types/one-to-many.md);
- Always the child entity's PK is a FK simultaneously;
- The mandatory end is always in the parent side, unless the child entity will be automatically created with the parent instance creation;

---
## Misleading usage / Common mistake

If you want to create a NON-parent-child relationship between entities, NEVER connect both PK directly, forcing one of them to be a FK simultaneously.

![](database/_basic-concepts/relationship-types/imgs/erd_inherits-not-needed.png)









---
