import json
import logging

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Organization, PaymentCard, Report
from .serializers import ReportSerializer
from .services import export_all_tenant_reports_csv, get_cached_analytics_data

logger = logging.getLogger(__name__)


def report_list(request: HttpRequest) -> HttpResponse:
    # Fine-grained Authorization：仅检查“是否登录”，不校验报表所属组织
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    keyword = request.GET.get("keyword", "")
    # 主漏洞：未按组织过滤，任意租户可看到所有租户报表
    reports = Report.objects.filter(title__icontains=keyword).select_related("organization", "created_by").order_by("-id")
    serializer = ReportSerializer(reports, many=True)
    return render(request, "report_list.html", {"reports": reports, "api_preview": serializer.data})


def create_report(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        org_name = request.POST.get("organization_name", "")
        api_key = request.POST.get("api_key", "")
        webhook_secret = request.POST.get("webhook_secret", "")
        title = request.POST.get("title", "")
        data_raw = request.POST.get("data", "{}")
        card_number = request.POST.get("card_number", "")
        cvv = request.POST.get("cvv", "")
        expiry_date = request.POST.get("expiry_date", "")

        creator, _ = User.objects.get_or_create(username=username, defaults={"email": f"{username}@demo.local"})
        organization, _ = Organization.objects.get_or_create(
            name=org_name,
            defaults={"owner": creator, "api_key": api_key, "webhook_secret": webhook_secret},
        )

        # 明文保存支付卡数据
        PaymentCard.objects.create(
            organization=organization,
            card_number=card_number,
            cvv=cvv,
            expiry_date=expiry_date,
        )

        try:
            parsed_data = json.loads(data_raw)
        except json.JSONDecodeError:
            parsed_data = {"raw": data_raw}

        Report.objects.create(
            organization=organization,
            title=title,
            data=parsed_data,
            created_by=creator,
        )
        return redirect("report_list")

    return render(request, "admin.html")


def analytics_view(request: HttpRequest) -> HttpResponse:
    keyword = request.GET.get("keyword", "")
    analytics = get_cached_analytics_data(keyword)
    # medium 问题：日志泄露报表 ID
    logger.info("analytics report ids: %s", [item["id"] for item in analytics])
    return render(request, "analytics.html", {"analytics": analytics, "keyword": keyword})


def export_view(request: HttpRequest) -> HttpResponse:
    # Data Export：无权限校验，任意用户可导出全租户数据
    if request.GET.get("download") != "1":
        return render(request, "export.html")

    csv_content = export_all_tenant_reports_csv()
    response = HttpResponse(csv_content, content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="all_reports.csv"'
    return response


def admin_page(request: HttpRequest) -> HttpResponse:
    organizations = Organization.objects.select_related("owner").all().order_by("id")
    cards = PaymentCard.objects.select_related("organization").all().order_by("id")
    return render(request, "admin.html", {"organizations": organizations, "cards": cards})


def reports_api(request: HttpRequest) -> JsonResponse:
    reports = Report.objects.select_related("organization", "created_by").all().order_by("-id")
    serializer = ReportSerializer(reports, many=True)
    return JsonResponse(serializer.data, safe=False)
