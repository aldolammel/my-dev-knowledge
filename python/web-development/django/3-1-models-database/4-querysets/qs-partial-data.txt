

QUERYSETS: FOR PARTIAL DATA

    Use only() and defer() for partial data:

        E.g
            # Only load specific fields
            users = User.objects.only('username', 'email')[:100]

            # Defer loading large fields
            users = User.objects.defer('large_text_field')[:100]