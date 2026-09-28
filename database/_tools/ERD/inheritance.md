#### Database > Tools > ERD > Relationship types
# Supertype/Subtype (inheritance)

---

**Before:**
1. [What is ERD and its basic](/database/_tools/ERD/_about.md)

---

In Crow's Foot (and ER modeling generally), when a child entity's PK is also the same attribute that's connected to the parent's PK, you're modeling a supertype/subtype relationship (specialization/generalization) that can be understood as inheritance.

---
## Cardinality between Parent and Child entities/tables:

![](database/_tools/ERD/imgs/erd_inherits.png)

**Notice:**
- To use the *Supertype/Subtype* benefits, the relationship type must be [one-to-one](/database/_tools/ERD/one-to-one.md) or [one-to-many](/database/_tools/ERD/one-to-many.md);
- In this kind of relationship, the child entity's PK always is a FK simultaneously;
- The "many" (Crow's foot symbol) side always requires to be connected directly in a FK (commonly something like `something_id`).
- Business rule: the mandatory end of a cardinality always is in the parent side, unless both sides are mandatory (when the child entity will be automatically created with the parent instance creation);
- Cardinality descriptions always are from the PK (parent entity) perspective to the FK (child entities), e.g., "plane extends to the model".

---
## Misleading usage / Common mistake

If you want to create a NON-parent-child relationship between entities, NEVER connect both PK directly, forcing one of them to be a FK simultaneously.

![](database/_tools/ERD/imgs/erd_inherits-not-needed.png)









---
