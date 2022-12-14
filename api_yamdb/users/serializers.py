from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import ROLES, User


class UserSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'bio', 'role')
