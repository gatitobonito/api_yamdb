from rest_framework import serializers

from reviews.models import Comment, Review
from rest_framework import serializers
from reviews.models import Category, Genre, Title, TitleGenre


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


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Review
        fields = '__all__'

    def get_rating(self, obj):
        average = sum(obj.score) / len(obj.score)
        return round(average, 0)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
