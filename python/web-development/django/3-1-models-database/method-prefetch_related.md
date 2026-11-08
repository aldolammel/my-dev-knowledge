#### Python > Django > Models > Methods
# `prefetch_related()` model method

---

The `prefetch_related()` is a method provided by Django's ORM (Object-Relational Mapper). It's part of the `django.db.models` module and only works with Django model [QuerySets](/python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md).

When you access related objects in a loop (like displaying all tags for each article), Django normally performs a separate db query for each item. `prefetch_related()` performs a separate query for the relationship and "joins" the results in Python, reducing database hits drastically.

It solves the N+1 query problem by fetching related objects in just 2 queries total, instead of 1 query per item.
### When to use this
**“Will I access this relation for every object in the result?”**
- Yep, and it returns one obj, use [select_related()](/python/web-development/django/3-1-models-database/method-select_related.md).
- Yep, and it returns many objs, use `prefetch_related()`.
- No, so you should use neither.

---
## WITHOUT `prefetch_related()` benefits:
```python
authors = models.Author.objects.all()   # 1 query for authors
for author in authors:           # If 100 authors:
    books = author.books.all()   # 100 queries (one per author)
# Total: 101 queries :(

```

---
## With `prefetch_related()` benefits:
```python
authors = models.Author.objects.all().prefetch_related('books')   # 1 query for authors
for author in authors:                                     # 1 query for ALL books
    books = author.books.all()                             # Uses cached data, NO additional queries
# Total: 2 queries :)

```

---
## Common use:
```python
# Blog posts with comments
posts = models.Post.objects.all().prefetch_related('comments')
# Categories with products
categories = models.Category.objects.all().prefetch_related('products')
# Users with their groups
users = models.User.objects.all().prefetch_related('groups')
```

---
## If no `related_name` arg, use reverse name:
Also read about `related_name` argument: [/python/web-development/django/3-1-models-database/arg-related_name](/python/web-development/django/3-1-models-database/arg-related_name.md)
```python
# Using default reverse name (NO related_name needed)
authors = models.Author.objects.all().prefetch_related('book_set')  # Django looks for: <modelname>_set'.
# Using custom related_name (if defined)
authors = models.Author.objects.all().prefetch_related('books')  # Much cleaner when related_name is defined in the model class.
```

---
## Per-row access, but you need filtering or ordering:
In Django, the `Prefetch()` object is used in `prefetch_related()` to give you fine-grained control over how related objects are fetched, avoiding the N+1 query problem while allowing you to filter, reorder, or assign a custom queryset to the prefetched relationship.
```python
from django.db.models import Prefetch

authors = models.Author.objects.prefetch_related(
    Prefetch(
        'article_set', 
        queryset=Article.objects.filter(status='published').order_by('-published_date'),
        to_attr='published_articles'
    )
)
```
---
## `select_related()` VS `prefetch_related()`
[/python/web-development/django/3-1-models-database/select_related-vs-prefetch_related](/python/web-development/django/3-1-models-database/select_related-vs-prefetch_related.md)





