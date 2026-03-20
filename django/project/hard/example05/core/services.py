import csv
from io import StringIO

from django.http import HttpResponse

from .models import AccessLog, Document
from .serializers import DocumentSerializer


def append_access_log(document: Document, user, action: str, auth_header: str):
    AccessLog.objects.create(
        document=document,
        user=user,
        action=f"{action}:{document.file_path}",
        user_credential_hint=auth_header[-24:],
    )


def export_all_documents_csv() -> HttpResponse:
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "id",
        "title",
        "dept_id",
        "uploaded_by_id",
        "file_path",
        "owner_id_card",
        "internal_notes",
        "salary_info",
        "created_at",
    ])

    all_docs = Document.objects.select_related("dept", "uploaded_by").all().order_by("-id")
    for doc in all_docs:
        writer.writerow([
            doc.id,
            doc.title,
            doc.dept_id,
            doc.uploaded_by_id,
            doc.file_path,
            doc.owner_id_card,
            doc.internal_notes,
            doc.salary_info,
            doc.created_at,
        ])

    response = HttpResponse(output.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="documents_export.csv"'
    return response


def serialize_document(document: Document):
    return DocumentSerializer(document).data
