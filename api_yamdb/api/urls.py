from django.urls import include, path
from rest_framework import routers
from .views import CommentViewSet, ReviewViewSet, CategoryViewSet, GenreViewSet, TitleViewSet


router = routers.DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/<title_id/reviews/<review_id>/comments/',
                CommentViewSet, basename='comments')
router.register(r'category', CategoryViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'title', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
