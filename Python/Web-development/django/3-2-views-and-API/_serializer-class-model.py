
"""
    DJANGO SERIALIZERS: CREATING A SERIALIZER CLASS

    When you create a serializer class, you are building up an API.

    >> Whole Django serialization roadmap:
        ./serializer.txt

    >> Example of a custom field for serializer class:
        ./serializer-creating-class-custom-fields.py
"""

# FILE: /apps/my_app/serializers.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Using Django Rest Framework:
# /Python/Web-development/django/component-libraries/django-rest-framework/
from rest_framework import serializers
from . import models

class ExampleModelSerializer(serializers.ModelSerializer):
    """Serializer for XXXXXXXXXXX content entries."""

    # Custom Fields (directly based on another serializer class):
    # Reserved space...

    # Custom Method Fields (SerializerMethodField):
    # my_serial_method = serializers.SerializerMethodField()  # Auto-calls get_my_serial_method()

    class Meta:
        # Which model class the data's coming from:
        model = models.ExampleModel
        # Which fields (attributes) specifically:
        fields = [
            "xxxxxx_field_1",
            "xxxxxx_field_2",
            # "reserved_space",  # Custom field
        ]
