from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .models import Department, Document, Organization
from .services import append_access_log, export_all_documents_csv, serialize_document
from .tasks import async_document_index


def document_list_page(request: HttpRequest) -> HttpResponse:
    docs = Document.objects.select_related("dept", "uploaded_by").all().order_by("-id")
    return render(request, "document_list.html", {"docs": docs})


def create_doc_page(request: HttpRequest) -> HttpResponse:
    depts = Department.objects.all().order_by("id")
    return render(request, "create_doc.html", {"depts": depts})


@require_http_methods(["POST"])
def create_document(request: HttpRequest) -> HttpResponse:
    username = request.POST.get("username", "")
    org_name = request.POST.get("org_name", "")
    dept_name = request.POST.get("dept_name", "")
    user, _ = User.objects.get_or_create(username=username, defaults={"email": f"{username}@demo.local"})
    org, _ = Organization.objects.get_or_create(name=org_name, defaults={"owner": user})
    dept, _ = Department.objects.get_or_create(org=org, name=dept_name)

    file_path = request.POST.get("file_path") or f"/srv/docs/{org.id}/{dept.id}/{request.POST.get('title', 'doc')}.pdf"

    doc = Document.objects.create(
        dept=dept,
        uploaded_by=user,
        title=request.POST.get("title", "untitled"),
        file_path=file_path,
        owner_id_card=request.POST.get("owner_id_card", ""),
        internal_notes=request.POST.get("internal_notes", ""),
        salary_info=request.POST.get("salary_info", ""),
    )
    append_access_log(doc, user, "create", request.headers.get("Authorization", ""))
    async_document_index(doc.id, doc.file_path)
    return redirect("document_list")


@require_http_methods(["GET", "DELETE"])
def get_document(request: HttpRequest, doc_id_path: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    if request.method == "DELETE":
        doc = get_object_or_404(Document, id=doc_id_path)
        doc.delete()
        return JsonResponse({"deleted": True, "doc_id": doc_id_path})

    doc = get_object_or_404(Document.objects.select_related("dept", "uploaded_by"), id=doc_id_path)
    append_access_log(doc, request.user, "read", request.headers.get("Authorization", ""))
    api_payload = serialize_document(doc)
    return render(request, "document_detail.html", {"doc": doc, "api_payload": api_payload})


@require_http_methods(["GET"])
def export_documents(request: HttpRequest) -> HttpResponse:
    return export_all_documents_csv()


def export_page(request: HttpRequest) -> HttpResponse:
    return render(request, "export.html")
