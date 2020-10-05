from django.db import models
from utils.repo_operators import SENTINEL, filter_sentinel
from ledger.models import Transaction


def get(pk):
    try:
        return Transaction.objects.get(pk=pk)
    except models.ObjectDoesNotExist:
        return None


def filter_(
    transaction_type=SENTINEL, contact_id=SENTINEL, amount=SENTINEL,
    created_by_id=SENTINEL, created_at__range=SENTINEL
):
    kwargs = filter_sentinel(locals().copy())
    return Transaction.objects.filter(**kwargs)


def create(amount, transaction_type, created_by_id, contact_id=SENTINEL):
    kwargs = filter_sentinel(locals().copy())
    return Transaction.objects.create(**kwargs)


def update(
    transaction_id, amount=SENTINEL, transaction_type=SENTINEL, contact_id=SENTINEL
):
    kwargs = filter_sentinel(locals().copy())
    kwargs.pop("transaction_id")

    Transaction.objects.filter(pk=transaction_id).update(**kwargs)
    return get(pk=transaction_id)
