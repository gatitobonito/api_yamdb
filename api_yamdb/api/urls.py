from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, ReviewViewSet, CategoryViewSet, GenreViewSet, TitleViewSet


router_v1 = DefaultRouter()
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router_v1.register(r'titles/<title_id/reviews/<review_id>/comments/',
                CommentViewSet, basename='comments')
router_v1.register(r'category', CategoryViewSet)
router_v1.register(r'genre', GenreViewSet)
router_v1.register(r'title', TitleViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
