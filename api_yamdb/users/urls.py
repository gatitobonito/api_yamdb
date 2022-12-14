from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from rest_framework import routers
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),

    # Полный адрес страницы регистрации - auth/signup/,
    # но префикс auth/ обрабатывется в головном urls.py
    path(
        'auth/signup/',
        views.SignUp.as_view(),
        name='signup'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
    path(
        'password_reset_form/',
        PasswordResetView.as_view(),
        name='password_reset_form'
    ),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
