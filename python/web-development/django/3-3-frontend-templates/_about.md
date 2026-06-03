#### Python > Django > Structure
# Templates

---

Unlike *Flask* that uses *Jinja2* as its template engine, Django has its on template engine called *DTL* (Django Template Language) that's absolutely inspired by *Jinja2*, making their syntax and concepts very similar.

Django is divided in 3 main parts: models, views, and templates. Templates are responsible for display the data to the user through a text or layout file such as an HTML page. All data rendered via templates came from a *views.py*. Unlike Models and Views, template is NOT a specific file but a folder structure and its content basically formed by HTML files. Templates are responsible for:
- Define the presentation layer of your application;
- Use template tags and filters to render data dynamically;
- Separate the presentation from the business logic.

Built-in template tags and filters: https://docs.djangoproject.com/en/5.0/ref/templates/builtins/

---

**OTHER DJANGO PARTS:**
- Views: [python/web-development/django/3-2-views-and-API/\_about](python/web-development/django/3-2-views-and-API/_about.md)
- Models: [python/web-development/django/3-1-models-database/1-models-knowledge](python/web-development/django/3-1-models-database/1-models-knowledge.md)

**EXTERNAL TEMPLATE/FRONT-END SOLUTIONS:**
- Vue: [javascript/web-development/frontend/vue/vue-knowledge/\_about](javascript/web-development/frontend/vue/vue-knowledge/_about.md)
- React: [javascript/web-development/frontend/react/react-knowledge/\_about](javascript/web-development/frontend/react/react-knowledge/_about.md)
- Angular: [javascript/web-development/frontend/angular/angular-knowledge/\_about](javascript/web-development/frontend/angular/angular-knowledge/_about.md)
