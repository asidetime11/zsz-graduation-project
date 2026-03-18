from django.shortcuts import get_object_or_404, redirect, render
from .models import ParcelRecord


def create_parcel(request):
    if request.method == "POST":
        rec = ParcelRecord.objects.create(
            name=request.POST.get("name", ""),
            phone=request.POST.get("phone", ""),
            id_card=request.POST.get("id_card", ""),
            address=request.POST.get("address", ""),
            parcel_no=request.POST.get("parcel_no", ""),
            status=request.POST.get("status", "pending"),
        )
        return redirect("parcel_detail", rec.id)
    return render(request, "register.html")


def parcel_detail(request, record_id):
    # 未做对象级权限校验
    record = get_object_or_404(ParcelRecord, pk=record_id)
    return render(request, "detail.html", {"record": record})
