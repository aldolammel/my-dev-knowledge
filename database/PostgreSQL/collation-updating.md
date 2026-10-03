#### Database > PostgreSQL
# Updating the collation version

---

Collation is the set of rules that decides how PostgreSQL compares and sorts text (strings). In simple words, it answers questions like:

- Is "São" equal to "sao"?
- Does "Árvore" come before or after "Abacaxi" when I do ORDER BY nome?
- Is "coop" different from "co-op" or "coöp"?

---
## Before    
1. Opening the Postgres shell:
	- Root user is 'postgres', so: `$ sudo -u postgres psql -d postgres`
	- List all databases: `$ \l`

---
## 1) Updating the Collation Version for desired db and templates:
```
ALTER DATABASE postgres REFRESH COLLATION VERSION;
ALTER DATABASE template1 REFRESH COLLATION VERSION;
ALTER DATABASE your_project_db_name REFRESH COLLATION VERSION;
```

**Notice:**
- `template0` cannot be updated, it's intentionally frozen!
- It's ok if some of db's say "*version has not changed*"!


---
## 2) Case you wanna leave the PostgreSQL shell:
```
\q
```

---
