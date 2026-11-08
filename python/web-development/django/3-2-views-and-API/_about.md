#### Python > Django > Structure
# `views.py`file

---

It's where endpoints logic is developed. Views are responsible for manage what data the user will see through a template, for example. The `views.py` file contains all logic the user can see, beyond to define which template/webpage the data will be seen.

- Views are responsible about what data users can read/see.
- Views also manage the data the front-end users can send to the database.
- `views.py` file is closely related with `urls.py` file, this one defining which view will be called in certain URL;
- Views are created through 2 ways apart:
	- [function-base view:](/python/web-development/django/3-2-views-and-API/1-building-views-context/function-based/view-func-basic-usage.py) known as FBVs.
	- [class-base view:](/python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/_views-class-basic.md) known as CBVs (recommended)

---
## In other words, `views.py`:
- Handles user input and interact with models to retrieve data;
- Renders templates (front-end) with the data obtained from models;
- Returns HTTP responses (like HTML, JSON, XML, etc).

---
## `views.py` are part of an API:
Once Views and [API](/api/_about.md) concepts share similarities, they are NOT the same even though both are responsible to send data from back-end to front-end, for example.

***Serializers* VS *Views*:**
Why not to create JSON directly with Views? A [serializer](/python/web-development/django/3-2-views-and-API/serializer.md) is a single, declarative place that owns the contract between your models and the JSON, in both directions. Building JSON by hand in *views* works for one endpoint, but it scales badly for non-super-simple apps.

---
## Other Django structural parts:
Django is divided in 3 main parts: models, views, and templates.
- Models: [/python/web-development/django/3-1-models-database/1-models-knowledge](/python/web-development/django/3-1-models-database/1-models-knowledge.md)
- Templates: [/python/web-development/django/3-3-frontend-templates/\_about](/python/web-development/django/3-3-frontend-templates/_about.md)

