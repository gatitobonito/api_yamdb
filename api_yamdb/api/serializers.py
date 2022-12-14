from rest_framework import serializers

from users.models import User
from reviews.models import Category, Genre, Title


class UserEmailRegistration(serializers.Serializer):
    """Класс сериализатор Email."""

    email = serializers.EmailField(required=True)


class UserConfirmation(serializers.Serializer):
    """Класс сериализатор подтверждение Email."""

    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'bio',
                  'role')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug']


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = [
            'id', 'name', 'year', 'description', 'genre', 'category']


class TitleSerializerCrUpDel(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True)
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug')

    class Meta:
        model = Title
        fields = ['id', 'name', 'year', 'description', 'genre', 'category']
