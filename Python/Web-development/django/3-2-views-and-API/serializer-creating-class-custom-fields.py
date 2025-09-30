
"""
    DJANGO SERIALIZERS: CREATING CUSTOM FIELDS DIRECTLY IN SERIALIZER CLASS

    >> Whole Django serialization roadmap:
        /Python/Web-development/django/3-2-views-and-API/serializer.txt
"""

class PagexMenuSerializer(serializers.ModelSerializer):
    """Creating the Pagex Menu API where all menus data is converted to JSON format."""

    # Custom Serializer Fields (based on another serializer class):
    links = PagexMenuLinkSerializer(many=True, read_only=True)

    # Custom Serializer Method Fields (SerializerMethodField):
    is_urls_relative = serializers.SerializerMethodField()  # Auto calls get_is_urls_relative()

    class Meta:
        model = PagexMenu
        fields = [
            "identifier",
            # - - - custom fields: - - -
            "is_urls_relative",  # This attr. exists only for serializer!
            "links",
        ]

    def get_is_urls_relative(self, obj):
        pagex_stgs = PagexSettings.objects.first()
        if pagex_stgs and hasattr(pagex_stgs, "is_urls_relative"):
            return pagex_stgs.is_urls_relative
        return "ERROR: get_is_urls_relative"