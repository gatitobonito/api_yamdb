from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)
# ROLES = (
#     (ADMIN, 'administrator'),
#     (MODERATOR, 'moderator'),
#     (USER, 'user'),
# )

class User(AbstractUser):
    username_validator = RegexValidator(r'^[\w.@+-]+')
    bio = models.TextField(
        blank=True,
    )
    role = models.CharField(
        max_length=16,
        choices=ROLES,
        default='user'
    )
    confirmation_code = models.CharField(max_length=60, blank=True)
    username = models.CharField(max_length=150, unique=True,
                                validators=[username_validator])
    email = models.EmailField(max_length=254, unique=True, blank=False)
    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_staff

    @property
    def is_moderator(self):
        return self.role == 'moderator'
