from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer, Serializer
from ledger.models import Transaction, TransactionType
from user_manager.serializers import UserSummarySerializer
from utils.choice import ChoiceField


class CreateTransactionSerializer(ModelSerializer):
    created_by_id = IntegerField()
    contact_id = IntegerField(required=False, allow_null=True)
    transaction_type = ChoiceField(labels=TransactionType.choices())

    class Meta:
        model = Transaction
        fields = ("amount", "contact_id", "transaction_type", "created_by_id", "client_timestamp")


class TransactionSerializer(ModelSerializer):
    transaction_type = ChoiceField(labels=TransactionType.choices())
    contact = UserSummarySerializer()

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "transaction_type",
            "contact",
            "created_by",
            "created_at",
            "updated_at"
        )
        read_only_fields = ("id", "created_at", "updated_at")


class TransactionFilterSerializer(Serializer):
    contact_id = IntegerField(required=False, allow_null=False)
    transaction_type = ChoiceField(labels=TransactionType.choices(), required=False, allow_null=False)
