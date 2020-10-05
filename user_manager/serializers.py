from rest_framework.fields import SerializerMethodField, CharField
from rest_framework.serializers import ModelSerializer, Serializer
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
        read_only_fields = ("id", "full_name", "is_admin")

    def get_is_admin(self, instance):
        return instance.is_admin()


class UserSummarySerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "full_name")


class UserFilterSerializer(Serializer):
    phone = CharField(required=False, allow_null=False)
