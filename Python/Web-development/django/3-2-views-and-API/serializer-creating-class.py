
"""
    DJANGO SERIALIZERS > DATA CONVERSION: CREATING A SERIALIZER CLASS

    When you create a serializer class, you are building up an API.

    >> Whole Django serialization roadmap:
        /Python/Web-development/django/3-2-views-and-API/serializer.txt
"""

# FILE: /apps/my_app/serializers.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Using Django Rest Framework:
# /Python/Web-development/django/component-libraries/django-rest-framework/
from rest_framework import serializers

class ExampleModelSerializer(serializers.ModelSerializer):
    """Serializer for XXXXXXXXXXX content entries."""

    # Custom Serializer Fields (based on another serializer class):
    # Reserved space...

    # Custom Serializer Method Fields (SerializerMethodField):
    # my_serial_method = serializers.SerializerMethodField()  # Auto-calls get_my_serial_method()

    class Meta:
        # Which model class the data's coming from:
        model = ExampleModel
        # Which fields (attributes) specifically:
        fields = [
            "slug",
            "is_published",
            # - - - custom fields: - - -
            # Reserved space...
        ]
