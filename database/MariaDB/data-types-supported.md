#### Database > MariaDB
# Data types supported

---

==**Last update:** 2026, September.==

---

It's organized by "category" followed by its data types available.

**Integer:**
- `TINYINT`
- `SMALLINT`
- `MEDIUMINT`
- `INT`
- `BIGINT`

**Exact decimal:**
- `DECIMAL`(alias: `NUMERIC`, `DEC`, `FIXED`)

**Floating point:**
- `FLOAT`
- `DOUBLE` (alias; `REAL`, `DOUBLE PRECISION`)

**Monetary:**
- E.g.`DECIMAL(19,4)`

**Boolean:**
- `BOOLEAN` / `BOOL` (actually they are `TINYINT(1)` for true)

**Fixed-length text:**
- `CHAR(n)`

**Variable text:**
- `VARCHAR(n)`
- `TINYTEXT`
- `TEXT`
- `MEDIUMTEXT`
- `LONGTEXT`

**Binary:**
- `BINARY`
- `VARBINARY`
- `TINYBLOB`
- `BLOB`
- `MEDIUMBLOB`
- `LONGBLOB`

**Date:**
- `DATE`
- `YEAR`

**Time:**
- `TIME`

**Date + time:**
- `DATETIME`
- `TIMESTAMP`

**UUID:**
- `UUID`

**JSON:**
- `JSON`

**Array:**
- ==Not supported!==

**Set:**
- `SET`

**Map/dictionary:**
- ==Not supported!==

**Enum:**
- `ENUM`

**Custom types:**
- Limited!

**Spatial:**
- `GEOMETRY`
- `POINT`
- `LINESTRING`
- `POLYGON`
- `MULTIPOINT`
- `MULTILINESTRING`
- `MULTIPOLYGON`
- `GEOMETRYCOLLECTION`

**Network:**
- `INET4` (IPv4)
- `INET6` (IPv6)

**Range:**
- ==Not supported!==

**XML:**
- ==Not supported!==

**Bit strings:**
- `BIT`

**Vector:**
- `VECTOR`

---
## Data types supported by other databases:

- PostgreSQL: [data-types-supported](/database/PostgreSQL/data-types-supported.md)
- MySQL: [data-types-supported](/database/MySQL/data-types-supported.md)
- SQLite: [data-types-supported](/database/SQLite/data-types-supported.md)
- CassandraDB: [data-types-supported](/database/CassandraDB/data-types-supported.md)
