from rest_framework import serializers
from django.core.validators import RegexValidator

from users.models import User
from reviews.models import Category, Genre, Title
from reviews.models import Comment, Review


class UserEmailRegistration(serializers.Serializer):
    NAME_VALIDATOR = RegexValidator(r'^[\w.@+-]+')
    email = serializers.EmailField(required=True, max_length=254)
    username = serializers.CharField(required=True, max_length=150, validators=[NAME_VALIDATOR])

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError(
                'Вы не можете зарегистрировать имя me')
        return value

class UserConfirmation(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio',
                  'role')


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User
        read_only_fields = ('role',)

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

    # def create(self, validated_data):
    #     if 'genre' not in self.initial_data:
    #         title = Title.objects.create(**validated_data)
    #         return title
    #     else:
    #         genres = validated_data.pop('genre')
    #         title = Title.objects.create(**validated_data)
    #         for genre in genres:
    #             current_genre, status = Genre.objects.get_or_create(
    #                 **genre
    #             )
    #             TitleGenre.objects.create(
    #                 genre=current_genre, title=title
    #             )
    #         return title
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.year = validated_data.get('year', instance.yearr)
    #     instance.description = validated_data.get(
    #         'description', instance.description
    #     )
    #     if 'genre' in validated_data:
    #         genre_data = validated_data.pop('genre')
    #         lst = []
    #         for genre in genre_data:
    #             current_genre, status = Genre.objects.get_or_create(
    #                 **genre
    #             )
    #             lst.append(current_genre)
    #         instance.genre.set(lst)
    #
    #     instance.save()
    #     return instance


class TitleSerializerCrUpDel(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True)
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug')

    class Meta:
        model = Title
        fields = ['id', 'name', 'year', 'description', 'genre', 'category']


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    class Meta:
        model = Review
        fields = '__all__'

    def get_rating(self, obj):
        average = sum(obj.score) / len(obj.score)
        return round(average, 0)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
