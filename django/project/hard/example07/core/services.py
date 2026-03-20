import csv
import json
from io import StringIO
from pathlib import Path

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse

from .models import AuditLog, BackupRecord, Transaction


def cache_report_data_with_card() -> list:
    cache_key = "report:transactions:full"
    cached = cache.get(cache_key)
    if cached:
        return cached

    rows = list(Transaction.objects.values("id", "user_id", "amount", "card_number", "status", "created_at").order_by("-id")[:100])
    cache.set(cache_key, rows)
    return rows


def export_audit_logs_csv() -> HttpResponse:
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "user_id", "action", "sql_snippet", "card_number", "timestamp"])
    for log in AuditLog.objects.all().order_by("-id"):
        writer.writerow([log.id, log.user_id, log.action, log.sql_snippet, log.card_number, log.timestamp])

    response = HttpResponse(output.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="audit_logs.csv"'
    return response


def create_plain_db_backup() -> str:
    backup_dir = settings.BASE_DIR / "db_backups"
    backup_dir.mkdir(exist_ok=True)
    file_path = backup_dir / "backup_plain_dump.json"

    payload = list(
        Transaction.objects.values("id", "user_id", "amount", "card_number", "status", "audit_trail", "created_at")
    )
    file_path.write_text(json.dumps(payload, ensure_ascii=False, default=str, indent=2), encoding="utf-8")
    BackupRecord.objects.create(file_path=str(file_path))
    return str(file_path)
