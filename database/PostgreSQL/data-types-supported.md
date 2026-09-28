#### Database > PostgreSQL
# Data types supported

---

==**Last update:** 2026, September.==

PostgreSQL has probably the richest native type system of those most db used.

---

It's organized by "category" followed by its data types available.

**Integer:**
- `smallint`
- `integer`
- `bigint`
- Shorthand macros:
	- `smallserial`
	- `serial`
	- `bigserial`

**Exact decimal:**
- `decimal` (`numeric` is an alias)

**Floating point:**
- `real`
- `double` `precision`

**Monetary:**
- `numeric`
- `money` (not a good option)

**Boolean:**
- `boolean`

**Fixed-length text:**
- `char(n)`/`character(n)`

**Variable text:**
- `varchar`/`varchar(n)`
- `text`

**Binary:**
- `bytea`

**Date:**
- `date`

**Time:**
- `time`

**Date + time:**
- `timestamp`
- `timestamptz` (with timezone included)

**UUID:**
- `uuid`

**JSON:**
- `json`
- `jsonb`
- `jsonpath`

**Array:**
- Native.

**Set:**
- ==Not supported!==

**Map/dictionary:**
- `jsonb`
- `hstore` extension!

**Enum:**
- `enum`

**Custom types:**
- Extensive!

**Spatial:**
- `point`
- `line`
- `lseg`
- `box`
- `path`
- `polygon
- `circle`
- PostGIS extension (real geospatial features (geography, SRIDs, spatial indexes and functions).

**Network:**
- `inet`
- `cidr`
- `macaddr`
- ...

**Range:**
- Native:
	- `int4range`
	- `int8range`
	- `numrange`
	- `tsrange`
	- `tstzrange`
	- `daterange`

**XML:**
- `xml`

**Bit strings:**
- `bit`
- `varbit`

**Vector:**
- `pgvector`

---
## Data types supported by other databases:

- MySQL: [data-types-supported](/database/MySQL/data-types-supported.md)
- MariaDB: [data-types-supported](/database/MariaDB/data-types-supported.md)
- SQLite: [data-types-supported](/database/SQLite/data-types-supported.md)
- CassandraDB: [data-types-supported](/database/CassandraDB/data-types-supported.md)
