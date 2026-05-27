from django.conf import settings as stgs
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = stgs.AUTH_USER_MODEL
        fields = ['url', 'username', 'email', 'is_staff']