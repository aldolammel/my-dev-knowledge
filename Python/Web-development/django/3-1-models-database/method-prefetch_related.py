

"""
    DJANGO'S ORM > METHODS: PREFETCH_RELATED()

    The 'prefetch_related()' is a method provided by Django's ORM (Object-Relational Mapper). It's part of the django.db.models module and only works with Django model QuerySets.
    
    When you access related objects in a loop (like displaying all tags for each article), Django normally performs a separate db query for each item. prefetch_related() performs a separate query for the relationship and "joins" the results in Python, reducing database hits drastically.

    It solves the N+1 query problem by fetching related objects in just 2 queries total, instead of 1 query per item.

    >> Also read about "related_name":
        ./arg-related_name.txt

"""

# Without prefetch_related benefits - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

authors = Author.objects.all()  # 1 query for authors
for author in authors:           # If 100 authors:
    books = author.books.all()   # 100 queries (one per author)
# Total: 101 queries :(


# With prefetch_related benefits - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

authors = Author.objects.all().prefetch_related('books')  # 1 query for authors
for author in authors:                                     # 1 query for ALL books
    books = author.books.all()   # Uses cached data, NO additional queries
# Total: 2 queries :)


# Common use - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Blog posts with comments
posts = Post.objects.all().prefetch_related('comments')

# Categories with products
categories = Category.objects.all().prefetch_related('products')

# Users with their groups
users = User.objects.all().prefetch_related('groups')


# If no related_name, use reverse name - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Using default reverse name (NO related_name needed)
authors = Author.objects.all().prefetch_related('book_set')  # Django looks for: <modelname>_set'.

# Using custom related_name (if defined)
authors = Author.objects.all().prefetch_related('books')  # Much cleaner when defined in the model.
# related_name:
# ./arg-related_name.txt