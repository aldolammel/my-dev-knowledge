#### Database > Tools > ERD
# Creating an ER Diagram

---

**Before:**
1. [What is ERD document](database/_tools/ERD/_about.md)
2. ERD tool (online and no-limit): https://app.diagrams.net

---

**Preparation:**
- [ ] Keep in mind to know what database system you'll use in this project is crucial to understand which data types to use through the ERD.
	- Remembering db data types:
		- [PostgreSQL](/database/PostgreSQL/data-types-supported.md)
		- [MariaDB](/database/MariaDB/data-types-supported.md)
		- [SQLite](/database/SQLite/data-types-supported.md)
		- [MySQL](/database/MySQL/data-types-supported.md)
		- [CassandraDB](/database/CassandraDB/data-types-supported.md)
- [ ] Trust me, much more efficient to think in the ERD looking an User Interface scratch with fields/information ideas drawn on the screen.
	- [ ] ==(Private, sorry):== CMS Wireframe model, /Drive/Projects/3_Model-Project/4-Engineering/MODEL_wireframes-CMS.excalidraw
- [ ]  ==(Private, sorry):== ERD model, /Drive/Projects/3_Model-Project/4-Engineering/MODEL_202XXX-ERD-clientName-appType-YearToRelease.drawio
- [ ] Remember what you must include in your document: [/database/\_tools/ERD/imgs/erd\_what-to-draw.png](/database/_tools/ERD/imgs/erd_what-to-draw.png)

**First sketch:** 
- [ ] Start drawing the entities of just one feature of your app idea (e.g. user registration).
	- [ ] Make sure all relationships have business rules and cardinality descriptions.
	- [ ] Once the first small piece of your app is sketched:
		- [ ] Colorize differently what entity represents a regular class/table and:
			- [ ] ...what represents a [junction table (map table)](/database/_tools/ERD/junction-table.md). It helps to pay more attention when many-to-many relationships show up and might mess everything. 
			- [ ] ...what represents a table used basically for [inheritance/supertype/subtype](/database/_tools/ERD/inheritance.md).
	- [ ] Make a smart use of the ERD space, don't mixing or placing the next feature logic to close of your first feature drawn. Keep them with a good margin in between.

**Heavy work:**
- [ ] Extend this approach for all other app pieces/features.
- [ ] Double-check with those main relationship cardinalities that are crossing the entire ERD document.

**Finishing:**
- [ ] Make sure business rules of the main relationships (those connect all crucial areas) are not abusing to mandatory one-to-one. Remember: sometimes is better to allow an crucial relationship to be `0:1..` and make it mandatory only by validations. It avoid an accidental deletion and a catastrophic delete_cascade in many other entity instances. Think about!

---
