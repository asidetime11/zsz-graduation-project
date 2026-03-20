import logging

from .models import PayrollTask


def shared_task(func):
    return func


logger = logging.getLogger(__name__)


@shared_task
def calculate_payroll(task_id: int):
    task = PayrollTask.objects.select_related("employee").filter(id=task_id).first()
    if not task:
        return {"ok": False}

    logger.info(
        "calculate_payroll employee=%s card_number=%s salary=%s amount=%s",
        task.employee.name,
        task.card_number,
        task.employee.salary,
        task.amount,
    )
    task.status = "done"
    task.task_log = f"processed card={task.card_number} salary={task.employee.salary}"
    task.save(update_fields=["status", "task_log"])
    return {"ok": True, "task": task.id}
