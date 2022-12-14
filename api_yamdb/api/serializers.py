from rest_framework import serializers


from users.models import User


class UserEmailRegistration(serializers.Serializer):
    """Класс сериализатор Email."""

    email = serializers.EmailField(required=True)


class UserConfirmation(serializers.Serializer):
    """Класс сериализатор подтверждение Email."""

    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # def create(self, validated_data):
    #     user = UserModel.objects.create_user(
    #         username=validated_data['username'],
    #         password=validated_data['password'],
    #     )
    #     return user


    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'bio', 'role')
