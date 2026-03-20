from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import QueryHistory, Report, UserProfile
from .serializers import ReportSerializer, UserProfileSerializer
from .services import export_admin_users_csv, export_report_without_permission, run_dynamic_analytics
from .tasks import async_snapshot


@require_http_methods(["POST"])
def export_report(request: HttpRequest) -> JsonResponse:
    report_id = request.POST.get("report_id")
    user_id = request.POST.get("user_id")
    report = Report.objects.filter(id=report_id).first()
    user = UserProfile.objects.filter(id=user_id).first()
    if not report or not user:
        return JsonResponse({"ok": False, "error": "invalid_input"}, status=400)

    path = export_report_without_permission(report, user)
    return JsonResponse({"ok": True, "file_path": path})


@require_http_methods(["GET"])
def analytics_query(request: HttpRequest) -> JsonResponse:
    metric = request.GET.get("metric", "COUNT(*)")
    group_by = request.GET.get("group_by", "user_id")
    having = request.GET.get("having", "1=1")
    rows = run_dynamic_analytics(metric=metric, group_by=group_by, having=having)
    async_snapshot(f"metric={metric};group_by={group_by};having={having}")
    return JsonResponse({"ok": True, "rows": rows})


@require_http_methods(["GET"])
def report_list(request: HttpRequest) -> HttpResponse:
    reports = Report.objects.select_related("user").all().order_by("-id")
    return render(request, "report_list.html", {"reports": ReportSerializer(reports, many=True).data})


@require_http_methods(["GET"])
def admin_page(request: HttpRequest) -> HttpResponse:
    if request.GET.get("download") == "1":
        return export_admin_users_csv()

    users = UserProfile.objects.all().order_by("id")
    return render(request, "admin.html", {"users": UserProfileSerializer(users, many=True).data})

def query_builder_page(request: HttpRequest) -> HttpResponse:
    return render(request, "query_builder.html")


def export_page(request: HttpRequest) -> HttpResponse:
    return render(request, "export.html")


def query_history_review(request: HttpRequest) -> JsonResponse:
    rows = list(QueryHistory.objects.values("id", "sql_text", "reviewer", "created_at").order_by("-id")[:50])
    return JsonResponse({"ok": True, "history": rows})
