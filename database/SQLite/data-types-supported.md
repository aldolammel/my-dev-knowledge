#### Database > SQLite
# Data types supported

---

==**Last update:** 2026, September.==

Instead of having a traditional collection of rigid column types, SQLite uses dynamic typing. The fundamental storage classes are only:
- `NULL`
- `INTEGER`
- `REAL`
- `TEXT`
- `BLOB`

SQLite doesn't natively have:
- `BOOLEAN`
- `DATE`
- `DATETIME`
- `UUID`
- `JSON`
- `ARRAY`
- `ENUM`

==(!!!)== **Types with this symbol** means the SQLite works very differently, so these are not equivalent to the corresponding types in the other databases.

---

It's organized by "category" followed by its data types available.

**Integer:**
- `INTEGER`

**Exact decimal:**
- `NUMERIC` ==(!!!)==

**Floating point:**
- `REAL`

**Monetary:**
- ??????????????????????????

**Boolean:**
- `INTEGER` using (`0`/`1`)  ==(!!!)==

**Fixed-length text:**
- `TEXT` ==(!!!)==

**Variable text:**
- `TEXT`

**Binary:**
- `BLOB``

**Date:**
- `TEXT`
- `INTEGER`
- `REAL` ==(!!!)==

**Time:**
- `TEXT`
- `INTEGER`
- `REAL` ==(!!!)==

**Date + time:**
- `TEXT`
- `INTEGER`
- `REAL` ==(!!!)==

**UUID:**
- `TEXT`
- `BLOB` ==(!!!)==

**JSON:**
- `TEXT` ==(!!!)==

**Array:**
- `TEXT` / `BLOB` or separate table! ==(!!!)==

**Set:**
- ==Not supported!==

**Map/dictionary:**
- ==Not supported!==

**Enum:**
- ==Not supported!==

**Custom types:**
- ==Not supported!==

**Spatial:**
- Extensions!

**Network:**
- ==Not supported!==

**Range:**
- ==Not supported!==

**XML:**
- ==Not supported!==

**Bit strings:**
- ==Not supported!==

**Vector:**
- ?????????????

---
## Data types supported by other databases:

- PostgreSQL: [data-types-supported](/database/PostgreSQL/data-types-supported.md)
- MySQL: [data-types-supported](/database/MySQL/data-types-supported.md)
- MariaDB: [data-types-supported](/database/MariaDB/data-types-supported.md)
- CassandraDB: [data-types-supported](/database/CassandraDB/data-types-supported.md)
