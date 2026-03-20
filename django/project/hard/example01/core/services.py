import csv
import io

from django.core.cache import cache

from .models import Report


def get_cached_analytics_data(keyword: str):
    cache_key = f"analytics:{keyword}"
    cached = cache.get(cache_key)
    if cached:
        return cached

    reports = list(
        Report.objects.filter(title__icontains=keyword).values(
            "id", "title", "organization_id", "organization__name", "data", "created_at"
        )
    )
    cache.set(cache_key, reports)
    return reports


def export_all_tenant_reports_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["organization_id", "organization_name", "report_id", "title", "data", "created_at"])

    for report in Report.objects.select_related("organization").all().order_by("id"):
        writer.writerow(
            [
                report.organization_id,
                report.organization.name,
                report.id,
                report.title,
                report.data,
                report.created_at,
            ]
        )

    return output.getvalue()
