from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.status import HTTP_400_BAD_REQUEST
from drf_yasg.utils import swagger_auto_schema
from ledger.interactors import transaction_interactor
from ledger.permissions import TransactionPermission
from ledger.serializers import TransactionSerializer, CreateTransactionSerializer, TransactionFilterSerializer


class TransactionViewSet(GenericViewSet):
    serializer_class = TransactionSerializer
    permission_classes = (AllowAny,)
    # permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [TransactionPermission]

    def get_queryset(self):
        return transaction_interactor.filter_transactions()

    @swagger_auto_schema(
        operation_description="List Transactions",
        operation_id="list_transaction",
        responses={200: TransactionSerializer()},
    )
    def list(self, request, *args, **kwargs):
        serializer = TransactionFilterSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        transactions = transaction_interactor.filter_transactions(**serializer.validated_data)

        page = self.paginate_queryset(transactions)
        serializer = TransactionSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create Transaction",
        operation_id='create_transaction',
        request_body=CreateTransactionSerializer(),
        responses={200: TransactionSerializer()}
    )
    def post(self, request):
        params = request.data.copy()
        params["created_by_id"] = request.user.id
        serializer = CreateTransactionSerializer(data=params)
        serializer.is_valid(raise_exception=True)

        if transaction_interactor.has_duplicate_transaction(**serializer.validated_data):
            return Response(status=HTTP_400_BAD_REQUEST)

        transaction = transaction_interactor.create_transaction(**serializer.validated_data)
        return Response(TransactionSerializer(instance=transaction).data)

    @swagger_auto_schema(
        operation_description="Get Transaction",
        operation_id="get_transaction",
        responses={200: TransactionSerializer()},
    )
    def retrieve(self, request, pk):
        transaction = self.get_object()
        return Response(TransactionSerializer(instance=transaction).data)

    @swagger_auto_schema(
        operation_description="Transaction Partial Update",
        operation_id="transaction_partial_update",
        request_body=TransactionSerializer(),
        responses={200: TransactionSerializer()},
    )
    def partial_update(self, request, pk):
        transaction = self.get_object()
        serializer = TransactionSerializer(instance=transaction, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        transaction = transaction_interactor.update_transaction(transaction_id=transaction.id, **serializer.validated_data)
        return Response(TransactionSerializer(instance=transaction).data)
