
"""
    DJANGO SERIALIZERS: CREATING CUSTOM FIELDS DIRECTLY IN SERIALIZER CLASS

    >> Whole Django serialization roadmap:
        ./serializer.txt
"""

class ExampleSerializer(serializers.ModelSerializer):

    # Custom Serializer Fields (based on another serializer class):
    links = ExampleLinkSerializer(many=True, read_only=True)

    # Custom Serializer Method Fields (SerializerMethodField):
    is_system_active = serializers.SerializerMethodField()  # Auto calls get_is_system_active()
    category_names = serializers.SerializerMethodField()  # Auto calls get_category_names()

    class Meta:
        model = Example
        fields = [
            "identifier",
            #"categories",  # category_names istead!
            # - - - custom fields: - - -
            "links",
            "is_system_active",  # This attr. exists only for serializer!
            "category_names",  # This attr. exists only for serializer!
        ]

    def get_is_system_active(self, obj):
        sys_stgs = ExampleSettings.objects.first()
        if sys_stgs and hasattr(sys_stgs, "is_system_active"):
            return sys_stgs.is_system_active
        return "ERROR: get_is_system_active"

    def get_category_names(self, obj):
        return list(obj.categories.values_list("name", flat=True))  # If empty, returns []