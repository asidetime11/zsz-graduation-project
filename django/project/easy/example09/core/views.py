from django.shortcuts import redirect, render
from .models import CouponUser


def claim(request):
    if request.method == "POST":
        CouponUser.objects.create(
            name=request.POST.get("name", ""),
            phone=request.POST.get("phone", ""),
            id_card=request.POST.get("id_card", ""),
            occupation=request.POST.get("occupation", ""),
            income_level=request.POST.get("income_level", ""),
            coupon_code=request.POST.get("coupon_code", ""),
        )
        return redirect("record_list")
    return render(request, "claim.html")


def record_list(request):
    records = CouponUser.objects.all().order_by("-id")
    return render(request, "record_list.html", {"records": records})
