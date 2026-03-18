from rest_framework import serializers
from . import models
from .utils import pagex_url_builder


class PagexPageSerializer(serializers.ModelSerializer):
    """Django Rest Framework creates Pagex Pages API where all the pages data is converted to JSON
    format."""

    # Custom Fields (directly based on another serializer class):
    # Reserved space...
    
    # Custom Method Fields (SerializerMethodField):
    # Reserved space...  # Automatically calls get_<custom_method_var>()
    
    class Meta:
        model = PagexPage
        fields = [
            'id',
            'title',
            'slug',
            'categories',
            'is_published',
            'is_home',
        ]


class PagexMenuLinkSerializer(serializers.ModelSerializer):
    """Django REST Framework organizes links of a menu to be used by PagexMenuSerializer."""

    # Custom Fields (directly based on another serializer class):
    # Reserved space...

    # Custom Method Fields (SerializerMethodField):
    title = serializers.SerializerMethodField()  # Auto-calls get_title()
    url = serializers.SerializerMethodField()  # Auto-calls get_url()
    url_target = serializers.SerializerMethodField()  # Auto-calls get_url_target()
    is_home = serializers.SerializerMethodField()  # Auto-calls get_is_home()

    class Meta:
        model = models.PagexMenuLink
        fields = [
            "link_type",
            "url",  # Custom method field
            "url_target",  # Custom method field
            "is_home",  # Custom method field
            "title",  # Custom method field # Business rule: Menus won't use seo_page_title!
        ]

    def get_title(self, obj):
        """Based on link_type, Django REST Framework defines what attr. It will be used as 'title' for links in Menus API."""
        if obj.link_type == "page" and obj.page:
            return obj.page.title  # For menus, keep 'title' instead of 'seo_page_title'.
        elif obj.link_type == "category" and obj.category:
            return obj.category.cat
        elif obj.link_type == "redirection" and obj.redirection:
            return obj.redirection.name
        return "PAGEX ERROR > PagexMenuLinkSerializer > Invalid link."

    def get_url(self, obj):
        """Based on link_type, Django REST Framework defines URL for each link in Menus API."""
        if obj.link_type == "page" and obj.page:
            return pagex_url_builder(obj.page, 2, "page")
        elif obj.link_type == "category" and obj.category:
            return pagex_url_builder(obj.category, 2, "category")
        elif obj.link_type == "redirection" and obj.redirection:
            return obj.redirection.url  # Always absolute urls.
        return ""

    def get_url_target(self, obj):
        """Checks if the link must be open in a new tab."""
        if obj and obj.link_type == "redirection" and obj.redirection.is_new_tab:
            return "_blank"
        return "_self"

    def get_is_home(self, obj):
        """Check if the linked page is set as home page."""
        if not obj.page or obj.link_type != "page":
            return False  # Categories and redirection links are never home!
        return obj.page.is_home


class PagexMenuSerializer(serializers.ModelSerializer):
    """Creating the Pagex Menu API where all menus data is converted to JSON format."""

    links = PagexMenuLinkSerializer(many=True, read_only=True, source='pagex_menu_links')

    class Meta:
        model = PagexMenu
        fields = [
            'slug_key',
            'links',
        ]


class RecursiveLinkSerializer(serializers.ModelSerializer):
    """xxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

    # Custom Fields (directly based on another serializer class):
    # Reserved space...
    
    # Custom Method Fields (SerializerMethodField):
    children = serializers.SerializerMethodField()  # Automatically calls get_children()

    class Meta:
        model = PagexMenuLink
        fields = [
            'id',
            'title',
            'url',
            'children',
        ]

    def get_children(self, obj):
        return RecursiveLinkSerializer(obj.children.all(), many=True).data
