DATABASE CONSTRAINTS: NOT NULL

---

Prevents a column from storing NULL.

E.g
```sql
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	email VARCHAR(255) NOT NULL
);
```
