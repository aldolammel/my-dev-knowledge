#### Database > Tools > ERD > Relationship types
# One-to-One
---

**Before:**
1. [What is ERD and its basic](/database/_tools/ERD/_about.md)

---

Shorthand: `1:1`

This the least common type of relationship, but it’s the easiest to visualize. In this relationship, there is one and only one record on each side of the relationship. Each row in a table is connected to a single row in another table. The only crucial detail to be aware is about the business rule: if a relationship-end is mandatory, define which one is mandatory.

![](database/_tools/ERD/imgs/erd_one-to-one.png)

Notice:
- The person has `none or one` ID card.
- The ID card belongs to `one` person (mandatory).
- Foreign key (FK) of this relationship must be always in the side that demands a mandatory data.
	- In a CMS, the `person` instance form will NOT show a `identity_card` field.
	- In a CMS, the `identity_card` instance form WILL show a `person` field for selection/edition.
- Cardinality descriptions always are from the PK perspective to the FK, e.g., "Person has an ID card".

## Other examples of one-to-one:

- In many places in the world, a spousal relationship is one-to-one. 
- Your address is related to a single ZIP code, and that ZIP code is connected to a single geographic area. 
- An employee of a company has a single base-pay rate. 
- Only one patron can have a copy of a library book checked out at a time. 
- A customer of a business has a single customer ID.
- A student ID for a school is connected to a single student. 
- Santa Claus is affiliated with a single holiday. 
- A driver generally has one license. 
- Most countries have one national flag and one capital city, though there are a few countries with two (e.g., Bolivia, Swaziland, and Honduras), and one country with three capitals (South Africa). Because of rare exceptions like this, database administrators need to carefully consider if a relationship should be set up as one-to-one.

---



