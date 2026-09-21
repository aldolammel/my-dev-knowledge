#### Python > Django > Structure
# Views.py

---

Django is divided in 3 main parts: models, views, and templates. Views are responsible for manage what data the user will see through a template. The 'views.py' file contains all logic the user can see and which template/webpage the data will be seen.

- Besides the Views are responsible about what data users can read/see, Views are also what manages the data the app's users can send to the database.
- The 'views.py' file is closely related with 'urls.py' file, this one defining which view will be called in certain URL;
- Views are created through two ways apart:
	- function-base view: known as FBVs.
	- class-base view: known as CBVs (recommended)
- Through 'views.py' file you:
	- Handle user input and interact with models to retrieve data;
	- Render templates with the data obtained from models;
	- Return HTTP responses (like HTML, JSON, XML, etc).

## API:
==Important!==
Once Views and API concepts share similarities, they are NOT the same even though both are responsible to send data from back-end to front-end, for example.

---

**OTHER DJANGO PARTS:**
- Models: [/python/web-development/django/3-1-models-database/1-models-knowledge](/python/web-development/django/3-1-models-database/1-models-knowledge.md)
- Templates: [/python/web-development/django/3-3-frontend-templates/\_about](/python/web-development/django/3-3-frontend-templates/_about.md)

