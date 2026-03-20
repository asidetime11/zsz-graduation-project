import logging

logger = logging.getLogger(__name__)


def shared_task(func):
    return func


@shared_task
def warmup_user_cache(user_id: int):
    logger.debug("warmup_user_cache user_id=%s", user_id)
    return {"ok": True}
