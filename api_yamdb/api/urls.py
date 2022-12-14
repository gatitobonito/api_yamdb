from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from .views import send_confirmation_code, get_jwt_token, UserViewSet
from .views import CategoryViewSet, GenreViewSet, TitleViewSet

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet)
v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'genres', GenreViewSet)
v1_router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    # path('v1/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),    # path(
    path('v1/auth/signup/', send_confirmation_code, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
