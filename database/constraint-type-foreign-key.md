DATABASE CONSTRAINTS: FOREIGN KEY

---

Ensures values in a column exist in another table’s column.

E.g
```sql
CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(id)
);
```
