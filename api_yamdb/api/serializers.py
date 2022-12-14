from rest_framework import serializers

from users.models import User
from reviews.models import Category, Genre, Title, TitleGenre


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
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'bio', 'role')

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

    def create(self, validated_data):
        if 'genre' not in self.initial_data:
            title = Title.objects.create(**validated_data)
            return title
        else:
            genres = validated_data.pop('genre')
            title = Title.objects.create(**validated_data)
            for genre in genres:
                current_genre, status = Genre.objects.get_or_create(
                    **genre
                )
                TitleGenre.objects.create(
                    genre=current_genre, title=title
                )
            return title

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.yearr)
        instance.description = validated_data.get(
            'description', instance.description
        )
        if 'genre' in validated_data:
            genre_data = validated_data.pop('genre')
            lst = []
            for genre in genre_data:
                current_genre, status = Genre.objects.get_or_create(
                    **genre
                )
                lst.append(current_genre)
            instance.genre.set(lst)

        instance.save()
        return instance

