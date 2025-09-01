from rest_framework import serializers
from .models import (
    PagexPage,
    PagexMenu,
    PagexMenuLink,
)
from .constants import VAL_FRONT_TOOL_VUE


class PagexPageSerializer(serializers.ModelSerializer):
    """Django Rest Framework creates Pagex Pages API where all the pages data is converted to JSON
    format."""

    # Custom Serializer Fields (based on another serializer class):
    # Reserved space...
    
    # Custom Serializer Method Fields (SerializerMethodField):
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

    # Custom Serializer Fields (based on another serializer class):
    # Reserved space...
    
    # Custom Serializer Method Fields (SerializerMethodField):
    title = serializers.SerializerMethodField()  # Automatically calls get_title()
    url = serializers.SerializerMethodField()  # Automatically calls get_url()

    class Meta:
        model = PagexMenuLink
        fields = [
            'id',
            'link_type',
            'url',
            'title',
            'position',
        ]

    def get_title(self, obj):
        """Based on link_type, Django REST Framework defines what attr. will be used as 'title' for
        links in Menus API."""
        if obj.link_type == 'page' and obj.page:
            return obj.page.title  # For menus, keep 'title' instead of 'seo_title'.
        elif obj.link_type == 'category' and obj.category:
            return obj.category.cat
        elif obj.link_type == 'redirection' and obj.redirection:
            return obj.redirection.name
        return 'PAGEX ERROR: Invalid link.'

    def get_url(self, obj):
        """Based on link_type, it defines the right path to build the link URL in Menus API."""
        if obj.link_type == 'page' and obj.page:
            return f'/{obj.page.slug}'
        elif obj.link_type == 'category' and obj.category:
            return f'/category/{obj.category.slug}'
        elif obj.link_type == 'redirection' and obj.redirection:
            return obj.redirection.url
        return ''


class PagexMenuSerializer(serializers.ModelSerializer):
    """Creating the Pagex Menu API where all menus data is converted to JSON format."""

    links = PagexMenuLinkSerializer(many=True, read_only=True)

    class Meta:
        model = PagexMenu
        fields = [
            'identifier',
            'links',
        ]


class RecursiveLinkSerializer(serializers.ModelSerializer):
    """xxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

    # Custom Serializer Fields (based on another serializer class):
    # Reserved space...
    
    # Custom Serializer Method Fields (SerializerMethodField):
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
