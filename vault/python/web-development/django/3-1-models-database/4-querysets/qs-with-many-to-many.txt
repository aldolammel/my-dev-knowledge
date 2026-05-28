

QUERYSETS: WITH MANY-TO-MANY

    Use prefetch_related() for Many-to-Many:

        E.g.
            # Prefetch related objects
            articles = Article.objects.prefetch_related('tags')[:10]
            for article in articles:
                print(article.tags.all())  # No additional queries



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

>> For Foreigner Keys:
    ./qs-with-foreigner-keys.txt