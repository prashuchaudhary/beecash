from datetime import timedelta
from ledger.repos import transaction_repo
from utils.datetime_converter import get_current_datetime
from utils.repo_operators import SENTINEL


get_transaction = transaction_repo.get
filter_transactions = transaction_repo.filter_
update_transaction = transaction_repo.update
create_transaction = transaction_repo.create


def has_duplicate_transaction(amount, transaction_type, created_by_id, contact_id=SENTINEL):
    datetime_range = (get_current_datetime() - timedelta(seconds=5), get_current_datetime())
    return filter_transactions(
        amount=amount, transaction_type=transaction_type, contact_id=contact_id,
        created_by_id=created_by_id, created_at__range=datetime_range
    ).exists()
