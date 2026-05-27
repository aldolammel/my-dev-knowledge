

DJANGO MODEL CLASS > ARGUMENT: DB_INDEX

    >> It works similarly to an index in a book, allowing the database to quickly locate rows without scanning the entire table. When you set db_index=True on a field in your Django model, Django will create a database index for that field when you run migrations. This can significantly speed up queries that filter, order, or perform lookups on that field.

        E.g. in models.py:

            class Product(models.Model):
                name = models.CharField(max_length=100, db_index=True)
