#### Python > Django
# Admin (CMS) in Django

---

The *admin.py* is an empty file automatically created by Django. It customize the logic to be used on CMS through its list-views and detail-views.

To simplify, the CMS is divided by this areas:
1. Home
2. List-view
3. Detail-view

---
## Home: 

It's a page where you get a resume of the CMS options:

http://localhost:8000/admin/

---
## List view: 

When you click on a CMS menu option, you'll be taken to a list page where 
all entries of one type of data in the database is shown. 

URL examples:
- Users list: http://localhost:8000/admin/auth/user/
- Pages list: http://localhost:8000/admin/pagex/pagexpage/

---
## Detail view:

When you click on an options listed in some List view, you'll be taken to a page with all data about that specific listed entry you previously have clicked.
### For existing object

E.g. how to check:
```
if obj:
	pass
```

URL examples:
- A specific User (obj) detail: http://localhost:8000/admin/auth/user/3/change/
- A specific Page (obj) detail: http://localhost:8000/admin/pagex/pagexpage/16/change/
### For new object

E.g. how to check:
```
if not obj:
	pass
```

URL examples:
- A new user (obj) detail: http://localhost:8000/admin/auth/user/add/
- A new page (obj) detail: http://localhost:8000/admin/pagex/pagexpage/add/
- How looks an Admin Class: [python/web-development/django/4-cms-admin/\_admin-class-model.py](python/web-development/django/4-cms-admin/_admin-class-model.py)
- What kind of CMS UX you need: [python/web-development/django/4-cms-admin/\_what-kind-of-cms-ux-do-you-need](python/web-development/django/4-cms-admin/_what-kind-of-cms-ux-do-you-need.md)


