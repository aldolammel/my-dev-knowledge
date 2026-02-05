
"""
    DJANGO SERIALIZERS: CREATING CUSTOM FIELDS DIRECTLY IN SERIALIZER CLASS

    >> Serialization roadmap:
        ./serializer.txt

    >> DSerializer class model:
        ./_serializer-class-model.py
    
    When you create a serializer class, you are building up an API endpoint, and, if needed, with custom fields to extract even more data to complement your API.

    >> Every serializers.py file demands:
        from rest_framework import serializers

    There are two ways to extract more data through a serializer class:
        A) Custom Method Field: uses a method-automatically-called to extract data elsewhere.
        B) Custom Field: uses another endpoint (serializer class) to collect more data.

        Examples A and B, below:
"""



# A) CUSTOM METHOD FIELDS (EXAMPLE 1/3) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# A very basic custom method field creation where the entire dataflow is examplefied:

# models.py
class Page(models.Model):
    id = ...
    title = ...
    is_blog = ...
class Post(models.Model):
    id = ...
    blog = ...  # menu dropdown to select some Page that is_blog = True
    title = ...
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, ...)

# serializers.py
class PostSerializer(serializers.ModelSerializer):

    # Custom Method Fields (SerializerMethodField):
    blog_name = serializers.SerializerMethodField()  # Auto calls get_blog_name()
    created_by_name = serializers.SerializerMethodField()  # Auto calls get_created_by_name()

    class Meta:
        model = models.Post
        fields = [
            # "blog",  # Output: e.g. 1 (id of the Page's obj, and not a blog name)
            "blog_name",  # Custom method field.
            # "created_by",  # Output: e.g. 3 (id of the User's obj, and not a name or username)
            "created_by_name",  # Custom method field.
        ]

    def get_blog_name(self, obj):
        if obj.blog:
            return obj.blog.title  # Output: e.g. "My Blog Name"
        return None

    def get_created_by_name(self, obj):
        if obj.created_by:
            if obj.created_by.get_full_name():
                return obj.created_by.get_full_name()  # Output: e.g. "John Doe"
            return obj.created_by.username  # Output: e.g. "johndoe1984"
        return None



# A) CUSTOM METHOD FIELDS (EXAMPLE 2/3) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# More examples of custom method, these ones returning list, dict, and even an argument value from another model, unlike the current model declared in the current serializer's Meta class:

# models.py:
class AppModel(models.Model):
    is_something_active = ...
class Pg(models.Model):
    title = ...
    categories = models.ManyToManyField("PgCategory",...)
    keywords = models.ManyToManyField("PgKeyword", ...)
class PgCategory(models.Model):
    name = ...
    slug = ...
class PgKeyword(models.Model):
    name = ...

# serializers.py:
class PgSerializer(serializers.ModelSerializer):

    # Custom Method Fields (SerializerMethodField):
    is_active = serializers.SerializerMethodField()  # Auto calls get_is_active()
    pg_categories = serializers.SerializerMethodField()  # Auto calls get_pg_categories()
    pg_keywords = serializers.SerializerMethodField()  # Auto calls get_pg_keywords()

    class Meta:
        model = models.Pg
        fields = [
            "title",
            #"categories",  # pg_categories istead!
            "is_active",  # Custom method field.
            "pg_categories",  # Custom method field.
            "pg_keywords",  # Custom method field.
        ]

    def get_is_active(self, obj):
        """Example of how to consult an attr status from another model not used in local Meta"""
        singleton = AppModel.objects.first()
        if singleton and hasattr(singleton, "is_something_active"):
            return singleton.is_something_active
        return "ERROR: get_is_active"

    def get_pg_categories(self, obj):
        """Returns a list with a dict of all page categories in (but if empty, returns [])"""
        return [{"name": cat.title, "slug": cat.slug} for cat in obj.categories.all()]

    def get_pg_keywords(self, obj):
        """Returns a list of all page keywords (but if empty, returns [])"""
        return list(obj.keywords.values_list("name", flat=True))



# A) CUSTOM METHOD FIELDS (EXAMPLE 3/3) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Using another endpoint (serializer) to collect even more data but already filtered:

# models.py
class Page(models.Model):
    title = ...
    slug = ...
    is_published = ...
    categories = models.ManyToManyField(
        "PageCategory",
        related_name="related_page_categories",
    )
class PageCategory(models.Model):
    name = ...
    slug = ...

# serializers.py
class CategoryDetailSerializer(serializers.ModelSerializer):  # serializer used to detail something
    class Meta:
        model = models.Page
        fields = [
            "title",
            "slug",
            "desc",
        ]

class CategorySerializer(serializers.ModelSerializer):  # main serializer what will be the endpoint!
    # Custom Method Fields (SerializerMethodField):
    related_pages = serializers.SerializerMethodField()  # Auto calls get_related_pages()

    class Meta:
        model = models.PageCategory
        fields = [
            "slug",
            "name",
            "related_pages",  # Custom method field
        ]

    def get_related_pages(self, obj):
        # This 'related_page_categories' comes from the PageModel's category attribute that has defined the 'related_name' argument:
        qs_published_pages = obj.related_page_categories.filter(is_published=True).order_by("title")
        return CategoryDetailSerializer(qs_published_pages, many=True).data



# B) EXAMPLE > CUSTOM FIELDS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Unlike the custom method field that uses a filtered data from another endpoint (serializer), using this custom field (not method) you can extract external data too, but without a custom queryset:

# models.py
class MenuLink(models.Model):
    """Each instance is a link in the app menus."""
    ...
class Menu(models.Model):
    """It manages which Menus exist through the app."""
    ...

# serializers.py
class MenuLinkSerializer(serializers.ModelSerializer):
    """It packages all links of a menu to be used by MenuSerializer."""
    ...
    class Meta:
        model = models.MenuLink
        ...
    ...

class MenuSerializer(serializers.ModelSerializer):
    """Creating the Menu API where all menus data is converted to JSON format."""

    # Custom Fields (directly based on another serializer class):
    all_menu_links = MenuLinkSerializer(many=True, read_only=True)

    class Meta:
        model = models.Menu
        fields = [
            ...
            "all_menu_links",  # Custom field
        ]
    ...