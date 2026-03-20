import logging

logger = logging.getLogger(__name__)


def shared_task(func):
    return func


@shared_task
def push_profile_snapshot(user_id: int, payload: dict):
    logger.info("push_profile_snapshot user_id=%s payload=%s", user_id, payload)
    return {"ok": True}
