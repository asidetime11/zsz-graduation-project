import logging

from .models import Transaction


def shared_task(func):
    return func


logger = logging.getLogger(__name__)


@shared_task
def process_transfer_async(transaction_id: int, card_number: str, cvv: str, amount: str):
    logger.info(
        "process transfer task id=%s card=%s cvv=%s amount=%s",
        transaction_id,
        card_number,
        cvv,
        amount,
    )
    tx = Transaction.objects.filter(id=transaction_id).first()
    if not tx:
        return {"ok": False, "reason": "missing transaction"}
    tx.status = "success"
    tx.save(update_fields=["status"])
    return {"ok": True, "transaction": transaction_id}
