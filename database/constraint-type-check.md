DATABASE CONSTRAINTS: CHECK

---

Ensures values satisfy a condition.

E.g
```sql
CREATE TABLE products (
	id SERIAL PRIMARY KEY,
	stock INT CHECK (stock >= 0)
);
```
