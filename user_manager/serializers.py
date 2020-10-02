from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from user_manager.models import User


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone")


class UserSerializer(ModelSerializer):
    is_admin = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone",
            "is_admin",
            "full_name",
            "last_name",
            "first_name",
        )

    def get_is_admin(self, instance):
        return instance.is_admin()
