
"""
    DJANGO MODELS > QUERYSETS: CREATING AGGREGATION

        >> What is it:
            ./_what-is-queryset.txt

        In these examples, consider each queryset is asking data to a model called 'Recipe':
"""


# Counting how many items/entries we got in 'Recipe' table:
count_the_entries = Recipe.objects.aggregate(Count('id'))

# Average of the price attribute (column) in Recipe table:
price_average = Recipe.objects.aggregate(Avg('price'))

# Sum of the price attribute (column) in Recipe table:
price_sum = Recipe.objects.aggregate(Sum('price'))

# Conditional result, using Local Operator 'OR' through Q class:
one_or_another = Recipe.objects.filter(
    models.Q(name__istartswith='a')
    or models.Q(description__icontains='salt')
)

# Counting how many items/entries we got (using Count Class):
total_class = Recipe.objects.aggregate(Count('id'))

# Counting how many items/entries we got (using Count Method):
total_method = Recipe.objects.all().count()

# Counting how many items/entries in a filter we got (using Count Method):
subtotal_method = Recipe.objects.filter(id__gt=5).count()

# Counting how many items/entries in a filter we got (using Count Class)
subtotal_class = Recipe.objects.filter(id__gt=5).aggregate(Count('id'))
