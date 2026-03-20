import logging

logger = logging.getLogger(__name__)


def shared_task(func):
    return func


@shared_task
def async_snapshot(sql_text: str):
    logger.info("async_snapshot sql=%s", sql_text)
    return {"ok": True}
