from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reviews.models import Category, Genre, Title
from users.models import User
from .filters import TitleFilter
from .permissions import IsAdmin, IsAdminOrReadOnly
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleSerializer,
                          TitleSerializerCrUpDel,
                          UserSerializer, UserEditSerializer,
                          UserConfirmation, UserEmailRegistration)
from .serializers import CommentSerializer, ReviewSerializer
from reviews.models import Comment, Review, TitleGenre

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_confirmation_code(request):
    serializer = UserEmailRegistration(data=request.data)
    serializer.is_valid(raise_exception=True)
    # serializer.save()
    # email = serializer.data.get('email')
    # user = User.objects.get_or_create(email=email)
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail("registration",
              f'Your confirmation code: {confirmation_code}',
              'admin@yamb.com',
              [user.email],
              fail_silently=False
              )
    return Response(serializer.data,
                    status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
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
    lookup_field = 'username'
    filter_backends = [filters.SearchFilter]
    # search_fields = ['user__username', ]
    search_fields = ('username',)
    permission_classes = (IsAdmin,)
    pagination_class = LimitOffsetPagination
    http_method_names = ['get', 'post', 'patch', 'delete']
    @action(methods=['patch', 'get'],
            permission_classes=[permissions.IsAuthenticated],
            serializer_class=UserEditSerializer,
            detail=False,
            url_path='me',
            )
    def edit_profile(self, request):
        user = self.request.user
        if self.request.method == 'GET':
            serializer = self.get_serializer(user)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(user,
                                             data=request.data,
                                             partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def perform_update(self, serializer):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    # def update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
    #     """Disallow full update (PUT) and allow partial update (PATCH)."""
    #     if kwargs.get("partial", False):  # Use .get() instead of .pop()
    #         return super().update(request, args, kwargs)
    #
    #     raise MethodNotAllowed(request.method)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    queryset = Title.objects.all()
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return TitleSerializerCrUpDel
        return TitleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(user=self.request.user, review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(user=self.request.user, title=title)