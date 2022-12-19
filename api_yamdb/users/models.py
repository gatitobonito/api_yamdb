from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CheckConstraint, Q, UniqueConstraint
from django.core.validators import RegexValidator

ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Админ'),
)


class User(AbstractUser):
    NAME_VALIDATOR = RegexValidator(r'^[\w.@+-]+')
    bio = models.TextField(
        blank=True,
    )
    role = models.CharField(
        max_length=150,
        choices=ROLES,
        default='user'
    )
    confirmation_code = models.CharField(max_length=60, blank=True)
    username = models.CharField(max_length=150, unique=True,
                                validators=[NAME_VALIDATOR]
                                )
    email = models.EmailField(max_length=254, unique=True, blank=False)

    class Meta:
        constraints = [
            CheckConstraint(
                name='username_not_me', check=~Q(username__iexact="me")
            ),
            UniqueConstraint(
                name='unique_user_email_pair', fields=['username', 'email']
            ),
        ]
