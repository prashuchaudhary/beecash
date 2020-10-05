from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema
from user_manager.interactors import user_interactor
from user_manager.permissions import UserPermission
from user_manager.serializers import UserSerializer, CreateUserSerializer, UserFilterSerializer


class UserViewSet(GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    # permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [UserPermission]

    def get_queryset(self):
        return user_interactor.filter_users()

    @swagger_auto_schema(
        operation_description="List Users",
        operation_id="list_user",
        responses={200: UserSerializer()},
    )
    def list(self, request, *args, **kwargs):
        serializer = UserFilterSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        users = user_interactor.filter_users(**serializer.validated_data)

        page = self.paginate_queryset(users)
        serializer = UserSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create User",
        operation_id='create_user',
        request_body=CreateUserSerializer(),
        responses={200: UserSerializer()}
    )
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_interactor.create_user(**serializer.validated_data)
        return Response(UserSerializer(instance=user).data)

    @swagger_auto_schema(
        operation_description="Get User",
        operation_id="get_user",
        responses={200: UserSerializer()},
    )
    def retrieve(self, request, pk):
        user = self.get_object()
        return Response(UserSerializer(instance=user).data)

    @swagger_auto_schema(
        operation_description="User Partial Update",
        operation_id="user_partial_update",
        request_body=UserSerializer(),
        responses={200: UserSerializer()},
    )
    def partial_update(self, request, pk):
        user = self.get_object()
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = user_interactor.update_user(user_id=user.id, **serializer.validated_data)
        return Response(UserSerializer(instance=user).data)
