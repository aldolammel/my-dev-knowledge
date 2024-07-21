

SEARCH FIELD:

    >> In your sub-app admin.py file, define which columns from a table should be available
        for searching:

        E.g.

            class MyTableExampleAdmin(admin.ModelAdmin):
                search_fields = ['attribute_name', 'another_one']

                