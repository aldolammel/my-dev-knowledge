DATABASE CONSTRAINTS: UNIQUE

---

Ensures all values in a column (or combination of columns) are unique.

E.g
```sql
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	email VARCHAR(255) UNIQUE
);
```

---
## Combining fields/columns to create the uniqueness
E.g.
```sql
CREATE TABLE procedures_procedure (
    id BIGSERIAL PRIMARY KEY,
    platform_id BIGINT NOT NULL REFERENCES platforms_platform (id),
    language_id BIGINT NOT NULL REFERENCES platforms_language (id),
    proc_type_id BIGINT NOT NULL REFERENCES procedures_proctype (id),
    created_by_id BIGINT NOT NULL REFERENCES accounts_user (id),

    CONSTRAINT unique_procedure_per_user_platform_language_type
        UNIQUE (platform_id, language_id, proc_type_id, created_by_id)
);
```


---
## Defining uniqueness with Python/Django:
[/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness](/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness.md)

