from django.contrib import admin
from reviews.models import Comment, Title, Genre, Category, TitleGenre, Review
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources



class GenreResource(resources.ModelResource):

    class Meta:
        model = Genre

class CommentResource(resources.ModelResource):

     class Meta:
        model = Comment



class TitleResource(resources.ModelResource):

    class Meta:
        model = Title


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category


class TitleGenreResource(resources.ModelResource):

    class Meta:
        model = TitleGenre
        filelds = (
            'id',
            'title_id',
            'genre_id'
        )


class ReviewResource(resources.ModelResource):

    class Meta:
        model = Review
        fields = (
            'id',
            'title_id',
            'text',
            'author',
            'score',
            'pub_date'
        )


class GenreAdmin(ImportExportActionModelAdmin):
    resource_class = GenreResource

class CommentAdmin(ImportExportActionModelAdmin):
    resource_class = CommentResource

class TitleAdmin(ImportExportActionModelAdmin):
    resource_class = TitleResource

class CategoryAdmin(ImportExportActionModelAdmin):
    resource_class = CategoryResource


class TitleGenreAdmin(ImportExportActionModelAdmin):
    resource_class = TitleGenreResource

class ReviewAdmin(ImportExportActionModelAdmin):
    resource_class = ReviewResource



admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TitleGenre, TitleGenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
