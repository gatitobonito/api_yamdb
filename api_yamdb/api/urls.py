from django.urls import include, path
from rest_framework import routers
from api.views import CommentViewSet, ReviewViewSet


router = routers.DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/<title_id/reviews/<review_id>/comments/',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]
