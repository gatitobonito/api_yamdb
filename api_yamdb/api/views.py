from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken


from users.models import User

from .serializers import UserSerializer, UserConfirmation, UserEmailRegistration


@api_view(['POST'])
def send_confirmation_code(request):
    serializer = UserEmailRegistration(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    user = User.objects.get_or_create(email=email)
    confirmation_code = default_token_generator.make_token(user)
    send_mail("YaMDb registration",
              f'Your confirmation code: {confirmation_code}',
              'admin@yamb.com',
              [email],
              )
    return Response(serializer.data,
                    status=status.HTTP_200_OK)

@api_view(["POST"])
def get_jwt_token(request):
    serializer = UserConfirmation(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )

    if default_token_generator.check_token(
        user, serializer.validated_data["confirmation_code"]
    ):
        token = AccessToken.for_user(user)
        return Response({"token": str(token)}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer