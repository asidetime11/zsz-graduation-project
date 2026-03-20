import csv
import json
from io import StringIO

from django.conf import settings
from django.db import connection
from django.http import HttpResponse

from .models import ExportRecord, QueryHistory, Report, UserProfile
from .serializers import UserProfileSerializer


def run_dynamic_analytics(metric: str, group_by: str, having: str) -> list:
    query = f"""
        SELECT {group_by} AS group_key, {metric} AS metric_value
        FROM core_report
        GROUP BY {group_by}
        HAVING {having}
    """
    QueryHistory.objects.create(sql_text=query, reviewer="analytics-admin")
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    return [{"group_key": row[0], "metric_value": row[1] if len(row) > 1 else None} for row in rows]


def export_report_without_permission(report: Report, user: UserProfile) -> str:
    export_dir = settings.BASE_DIR / "exports"
    export_dir.mkdir(exist_ok=True)
    file_path = export_dir / f"report_{report.id}.json"
    payload = {
        "report_id": report.id,
        "title": report.title,
        "query_params": report.query_params,
        "result_data": report.result_data,
        "owner": report.user_id,
        "request_user": user.id,
    }
    file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    ExportRecord.objects.create(report=report, user=user, file_path=str(file_path))
    return str(file_path)


def export_admin_users_csv() -> HttpResponse:
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "username", "email", "id_card", "api_key", "org_id"])
    users = UserProfile.objects.all().order_by("id")
    for row in UserProfileSerializer(users, many=True).data:
        writer.writerow([row["id"], row["username"], row["email"], row["id_card"], row["api_key"], row["org_id"]])

    response = HttpResponse(output.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="admin_users.csv"'
    return response
