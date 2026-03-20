import logging

logger = logging.getLogger(__name__)


def shared_task(func):
    return func


@shared_task
def mirror_audit_log(raw_sql: str, card_number: str, password_hash: str):
    logger.debug("mirror_audit_log sql=%s card_number=%s password_hash=%s", raw_sql, card_number, password_hash)
    return {"ok": True}
