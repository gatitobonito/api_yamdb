from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet
router_v1 = DefaultRouter()

router_v1.register(r'category', CategoryViewSet)
router_v1.register(r'genre', GenreViewSet)
router_v1.register(r'title', TitleViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
