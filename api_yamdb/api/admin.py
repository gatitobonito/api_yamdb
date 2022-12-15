from django.contrib import admin
from reviews.models import Comment, Title, Genre, Category, TitleGenre, Review

# Register your models here.
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(TitleGenre)
admin.site.register(Review)
admin.site.register(Comment)
