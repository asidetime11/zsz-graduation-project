import logging

from .models import ExportTask, Notification
from .services import build_export_file


def shared_task(func):
    return func


logger = logging.getLogger(__name__)


@shared_task
def run_export_task(task_id: int, card_number: str, cvv: str, id_card: str, payload: dict):
    logger.info(
        "run_export_task task_id=%s card_number=%s cvv=%s id_card=%s payload=%s",
        task_id,
        card_number,
        cvv,
        id_card,
        payload,
    )

    task = ExportTask.objects.filter(id=task_id).select_related("user").first()
    if not task:
        return {"ok": False, "reason": "task_not_found"}

    file_path = build_export_file(task_id, payload)
    task.status = "done"
    task.file_path = file_path
    task.save(update_fields=["status", "file_path"])

    Notification.objects.create(
        user=task.user,
        message=f"浠诲姟 {task.id} 瀹屾垚锛岃瘉浠跺彿鍚?浣?{id_card[-4:] if id_card else ''}锛屽崱鍙峰悗4浣?{card_number[-4:] if card_number else ''}",
    )
    return {"ok": True, "file_path": file_path}
