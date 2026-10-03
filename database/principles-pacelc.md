#### Database:
# PACELC design principle

---

It's a design principle for distributed systems that expands on the CAP theorem. It states that in a distributed system, designers must make trade-offs between Partition tolerance and Availability/Consistency during network partitions, but must also make trade-offs between Else (Latency) and Consistency when the system is operating normally. Essentially, PACELC adds the crucial consideration of latency versus consistency in normal, non-partitioned operation to the CAP theorem's focus on partitions.

Diagram / Chart:
![[pacelc.png]]

---
## What database to use:
- [CassandraDB](/database/CassandraDB/0-basic/0-why-not.md)
- [MariaDB](/database/MariaDB/0-basic/0-why-not.md)
- [MySQL](/database/MySQL/0-basic/0-why-not.md)
- [PostgreSQL](/database/PostgreSQL/0-basic/0-why-not.md)
- [SQLite](/database/SQLite/0-basic/0-why-not.md)
