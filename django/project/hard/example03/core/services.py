import json
from pathlib import Path

from django.conf import settings


def build_export_file(task_id: int, payload: dict):
    tmp_dir = Path("/tmp")
    if not tmp_dir.exists():
        tmp_dir = settings.BASE_DIR / "tmp_exports"
        tmp_dir.mkdir(exist_ok=True)

    file_path = tmp_dir / f"export_task_{task_id}.json"
    file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(file_path)
