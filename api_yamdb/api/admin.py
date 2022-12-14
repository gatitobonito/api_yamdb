from django.contrib import admin
from reviews.models import Title, Genre, Category, TitleGenre

# Register your models here.
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(TitleGenre)
