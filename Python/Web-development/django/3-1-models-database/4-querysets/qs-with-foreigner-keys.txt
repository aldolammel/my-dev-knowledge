

QUERYSETS: WITH FOREIGNER KEYS

    Use select_related() for Foreign Keys:

        E.g.
            # Avoids N+1 queries
            users = User.objects.select_related('profile')[:10]
            for user in users:
                print(user.profile.bio)  # No additional queries



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

>> For Many-to-Many:
    ./qs-with-many-to-many.txt