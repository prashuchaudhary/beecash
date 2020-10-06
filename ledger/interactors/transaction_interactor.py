from ledger.repos import transaction_repo
from utils.repo_operators import SENTINEL


get_transaction = transaction_repo.get
filter_transactions = transaction_repo.filter_
update_transaction = transaction_repo.update
create_transaction = transaction_repo.create


def has_duplicate_transaction(amount, transaction_type, created_by_id, client_timestamp, contact_id=SENTINEL):
    return filter_transactions(
        amount=amount, transaction_type=transaction_type, created_by_id=created_by_id,
        client_timestamp=client_timestamp, contact_id=contact_id,
    ).exists()
