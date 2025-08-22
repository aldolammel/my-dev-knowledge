# FILTERING:

# Showing the first entry on this model/table (Recipe):
r_first = Recipe.objects.first()

# Showing the entry with pk/id = 4:
r_specific = Recipe.objects.get(id=4)

# Showing all objects in a specific table (Recipe):
r_all = Recipe.objects.all()

# Showing a specific number of entries:
r_three = Recipe.objects.all()[:3]
""" Using the slicing technic. """

# Showing all entries greater than a value:
greater_than = Recipe.objects.filter(id__gt=3)
""" This 'id__' is the column (attribute) you want to search, 
and that '__gt' means 'greater than' command. 
You can use '__gte' for 'greater than or equal to' command."""

# Collecting all posts from the same user and created in the same date or later:
user_posts = Recipe.objects.filter(
    created_at__gte=instance.created_at,
    created_by=instance.created_by,
).exclude(pk=instance.pk)

# Filtering only entries from a specific category:
all_from_cat = Recipe.objects.filter(category__name__iexact='salad')
""" This 'i' before 'exact' means the search must not be case-sensitive. 
'category__name__exact' is case-sensitive. 
Be aware 1: this '__name__' is exactly the attribute the filter will be applied.
If you're looking for 'author' it must be written as '__author__'.
Be aware 2: not sure, but maybe the 'category__' is editable too."""

# Filtering only entries that contain a certain string in its name:
search_in_cat = Recipe.objects.filter(category__name__icontains='soup')
""" This 'i' before 'contains' means the search must not be case-sensitive.
'category__name__contains' is case-sensitive.
Be aware 1: this '__name__' is exactly the attribute the filter will be applied.
If you're looking for 'author' it must be written as '__author__'.
Be aware 2: not sure, but maybe the 'category__' is editable too."""

# Filtering only entries that DON'T contain a certain string in its name:
exclude_those = Recipe.objects.exclude(name__icontains='soup')
""" This 'i' before 'contains' means the search must not be case-sensitive.
'name__contains' is case-sensitive.
Be aware: this 'name__' is exactly the attribute the exclude will be applied.
If you're looking for 'author' it must be written as 'author__contains'."""

# Filtering even more:
super_search = Recipe.objects.exclude(name__icontains='soup').order_by('-date_added')
""" This '-date_added' is asking for descending order of date_added. """

# RETURNING OTHER FORMATS:

# Return as object (default):
as_obj = Recipe.objects.filter(id=7)
""" Output: <QuerySet [<Recipe: African Chicken Curry>]> """

# Return as dictionary:
as_dict = Recipe.objects.filter(id=7).values()
""" Output: 
    <QuerySet [
        {
            'id': 7, 
            'name': 
            'African Chicken Curry', 
            'description': 'Are you ready!', 
            'date_added': datetime.datetime(
                2024, 
                7, 
                3, 
                15, 
                29, 
                41, 
                39059, 
                tzinfo=datetime.timezone.utc
            ), 
            'category_id': 1
        }
    ]> 
"""

# Return as tuple:
as_tuple = Recipe.objects.filter(id=7).values_list()
""" Output: 
    <QuerySet [
        (
            7, 
            'African Chicken Curry', 
            'Are you ready!', 
            datetime.datetime(
                2024, 
                7, 
                3, 
                15, 
                29, 
                41, 
                39059, 
                tzinfo=datetime.timezone.utc
            ), 
            1
        )
    ]>
"""

# Return as boolean:
as_bool = Recipe.objects.filter(id=7).exists()
""" Output: True """
