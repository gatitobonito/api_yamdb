from django.core.validators import RegexValidator


def validate_username(username):
    NAME_VALIDATOR = RegexValidator(r'^[\w.@+-]+')
