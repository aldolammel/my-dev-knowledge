
"""
    DJANGO SERIALIZERS: CREATING CUSTOM FIELDS DIRECTLY IN SERIALIZER CLASS

    When you create a serializer class, you are building up an API, and, if needed, with custom fields that exist just through serializer class.
   
    >> Whole Django serialization roadmap:
        ./serializer.txt

    >> Or if you just want to a simple serializer class model:
        ./_serializer-class-model.py
"""

# Example 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class ExampleSerializer(serializers.ModelSerializer):

    # Custom Serializer Fields (based on another serializer class):
    links = ExampleLinkSerializer(many=True, read_only=True)

    # Custom Serializer Method Fields (SerializerMethodField):
    is_system_active = serializers.SerializerMethodField()  # Auto calls get_is_system_active()
    category_names = serializers.SerializerMethodField()  # Auto calls get_category_names()

    class Meta:
        model = models.Example
        fields = [
            ...
            "identifier",
            #"categories",  # category_names istead!
            "links",  # Custom field.
            "is_system_active",  # Custom field. This attr. exists only for serializer!
            "category_names",  # Custom field. This attr. exists only for serializer!
        ]

    def get_is_system_active(self, obj):
        sys_stgs = ExampleSettings.objects.first()
        if sys_stgs and hasattr(sys_stgs, "is_system_active"):
            return sys_stgs.is_system_active
        return "ERROR: get_is_system_active"

    def get_category_names(self, obj):
        return list(obj.categories.values_list("name", flat=True))  # If empty, returns []



# Example 2 (Sending not just id but the attribute name too) - - - - - - - - - - - - - - - - - - - -
class PostSerializer(serializers.ModelSerializer):

    # Custom Serializer Fields (based on another serializer class):
    # Reserved space...

    # Custom Serializer Method Fields (SerializerMethodField):
    blog_name = serializers.SerializerMethodField()  # Auto calls get_blog_name()
    created_by_name = serializers.SerializerMethodField()  # Auto calls get_created_by_name()

    class Meta:
        model = models.Example
        fields = [
            ...
            "blog",  # Output: e.g. 1
            "blog_name",  # Custom field. This attr. exists only for serializer!
            "created_by",  # Output: e.g. 3
            "created_by_name",  # Custom field. This attr. exists only for serializer!
        ]

    def get_blog_name(self, obj):
        if obj.blog:
            return obj.blog.title  # Output: "My Blog Name"
        return None

    def get_created_by_name(self, obj):
        if obj.created_by:
            if obj.created_by.get_full_name():
                return obj.created_by.get_full_name()  # Output: "John Doe"
            return obj.created_by.username  # Output: "johndoe1984"
        return None