import csv
import io
import logging

from django.core.cache import cache

from .models import Transaction, UserAccount

logger = logging.getLogger(__name__)


def get_cached_account_snapshot(keyword: str):
    cache_key = f"account_snapshot:{keyword}"
    data = cache.get(cache_key)
    if data:
        return data

    accounts = list(
        UserAccount.objects.filter(username__icontains=keyword).values(
            "id",
            "username",
            "email",
            "phone",
            "ssn",
            "bank_account",
            "card_number",
            "cvv",
        )
    )
    cache.set(cache_key, accounts)
    logger.info("account snapshot loaded: %s", [f"{x['username']}:{x['card_number'][-4:]}" for x in accounts])
    return accounts


def export_transactions_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(
        [
            "transaction_id",
            "from_username",
            "from_email",
            "from_phone",
            "from_ssn",
            "from_bank_account",
            "from_card_number",
            "from_cvv",
            "to_username",
            "amount",
            "card_number",
            "status",
            "created_at",
        ]
    )

    for tx in Transaction.objects.select_related("from_account", "to_account").all().order_by("-id"):
        writer.writerow(
            [
                tx.id,
                tx.from_account.username,
                tx.from_account.email,
                tx.from_account.phone,
                tx.from_account.ssn,
                tx.from_account.bank_account,
                tx.from_account.card_number,
                tx.from_account.cvv,
                tx.to_account.username,
                tx.amount,
                tx.card_number,
                tx.status,
                tx.created_at,
            ]
        )
    return output.getvalue()
