from rest_framework import serializers
from django.core.validators import RegexValidator
from django.shortcuts import get_object_or_404

from users.models import User
from reviews.models import (Category, Comment, Genre, Title,
                            Review)


class UserEmailRegistration(serializers.Serializer):
    NAME_VALIDATOR = RegexValidator(r'^[\w.@+-]+')
    email = serializers.EmailField(required=True,
                                   max_length=254,
                                   )
    username = serializers.CharField(required=True,
                                     max_length=150,
                                     validators=[NAME_VALIDATOR]
                                     )

    def validate(self, value):
        user1 = User.objects.filter(email=value['email'])
        if user1.exists():
            user2 = User.objects.filter(username=value['username'])
            if not user2.exists():
                raise serializers.ValidationError(
                    'Вы не можете зарегистрировать другое имя')
            # if get_object_or_404(User, email=value['email']).username != value['username']:
            #     raise serializers.ValidationError(
            #         'Вы не можете зарегистрировать другое имя')
        if value['username'].lower() == 'me':
            raise serializers.ValidationError(
                'Вы не можете зарегистрировать имя me')
        return value


    # def validate_username(self, value):
    #     if value.lower() == 'me':
    #         raise serializers.ValidationError(
    #             'Вы не можете зарегистрировать имя me')
    #     return value



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
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug']
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = [
            'id', 'name', 'year', 'description',
            'genre', 'category'
        ]


class TitleSerializerCrUpDel(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True)
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug')

    class Meta:
        model = Title
        fields = ['id', 'name', 'year',
                  'description', 'genre', 'category'
                  ]


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
        fields = [
            'id', 'text', 'author', 'score', 'pub_date', 'title']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'

    )

    class Meta:
        model = Comment
        fields = [
            'id', 'text', 'author', 'pub_date']
