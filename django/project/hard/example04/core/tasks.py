import logging

from .services import refresh_cache_without_ttl


def shared_task(func):
    return func


logger = logging.getLogger(__name__)


@shared_task
def async_refresh_sensitive_cache(user_id: int):
    data = refresh_cache_without_ttl(user_id)
    logger.info("async_refresh_sensitive_cache user_id=%s payload=%s", user_id, data)
    return data
