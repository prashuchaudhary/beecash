from django.db import models
from beecash import settings
from utils.choice import Choice


class TransactionType(Choice):
    DEBIT = 1
    CREDIT = 2


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.PositiveSmallIntegerField(choices=TransactionType.choices())
    contact = models.ForeignKey('user_manager.User', on_delete=models.PROTECT, null=True, blank=True)
    client_timestamp = models.BigIntegerField()

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('amount', 'transaction_type', 'contact', 'client_timestamp')
