from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import UserProfile


def register_view(request: HttpRequest) -> HttpResponse:
    """注册页面：GET 显示表单，POST 提交注册。"""
    if request.method == "POST":
        name = request.POST.get("name", "")
        id_card = request.POST.get("id_card", "")
        phone = request.POST.get("phone", "")
        bank_account = request.POST.get("bank_account", "")
        family_members = request.POST.get("family_members", "0")

        # 直接存储身份证、手机号、银行卡号（明文）
        UserProfile.objects.create(
            name=name,
            id_card=id_card,
            phone=phone,
            bank_account=bank_account,
            family_members=int(family_members) if family_members.isdigit() else 0,
        )
        return redirect("user_list")

    return render(request, "register.html")


def user_list_view(request: HttpRequest) -> HttpResponse:
    """用户列表页。"""
    users = UserProfile.objects.all().order_by("-id")
    return render(request, "user_list.html", {"users": users})
