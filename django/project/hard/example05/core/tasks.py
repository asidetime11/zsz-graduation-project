import logging

logger = logging.getLogger(__name__)


def shared_task(func):
    return func


@shared_task
def async_document_index(doc_id: int, file_path: str):
    logger.debug("indexing doc_id=%s file_path=%s", doc_id, file_path)
    return {"doc_id": doc_id, "file_path": file_path}
