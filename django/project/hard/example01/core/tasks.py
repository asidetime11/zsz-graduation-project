import logging

from django.core.cache import cache

from .models import Report


def shared_task(func):
    return func


logger = logging.getLogger(__name__)


@shared_task
def warm_analytics_cache(report_id: int):
    report = Report.objects.filter(id=report_id).values("id", "organization_id", "title", "data").first() or {}
    cache_key = f"analytics:latest:{report.get('title', '')}"
    payload = {
        "id": report.get("id"),
        "organization_id": report.get("organization_id"),
        "title": report.get("title"),
        "data": report.get("data"),
    }
    cache.set(cache_key, payload)
    logger.info("warm cache for report_id=%s", report_id)
    return payload
