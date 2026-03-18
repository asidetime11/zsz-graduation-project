from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Order, User
from .serializers import OrderSerializer, UserSerializer


def order_list(request: HttpRequest) -> HttpResponse:
    status = request.GET.get("status")
    min_price = request.GET.get("min_price")
    orders = Order.objects.select_related("user").all().order_by("-id")

    if status:
        orders = orders.filter(status=status)
    if min_price:
        orders = orders.filter(total_price__gte=min_price)

    serializer = OrderSerializer(orders, many=True)  # fields="__all__"，过度暴露字段
    return render(request, "order_list.html", {"orders": orders, "api_preview": serializer.data})


def order_detail(request: HttpRequest, order_id_path: int) -> HttpResponse:
    # 主漏洞：仅按 URL 参数查询订单，无任何当前用户归属校验
    order = Order.objects.get(id=order_id_path)
    return render(request, "order_detail.html", {"order": order})


def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        id_card = request.POST.get("id_card", "")
        passport_no = request.POST.get("passport_no", "")

        user, _ = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "phone": phone,
                "id_card": id_card,
                "passport_no": passport_no,
            },
        )

        # Missing Consent：未记录用户同意数据处理
        Order.objects.create(
            user=user,
            items=request.POST.get("items", ""),
            total_price=request.POST.get("total_price", "0"),
            address=request.POST.get("address", ""),
            payment_card=request.POST.get("payment_card", ""),
            status=request.POST.get("status", "pending"),
            passport_no=request.POST.get("passport_no", ""),
        )
        return redirect("order_list")

    return render(request, "create_order.html")


def users_api(request: HttpRequest) -> JsonResponse:
    users = User.objects.all().order_by("-id")
    serializer = UserSerializer(users, many=True)  # fields="__all__" 导致敏感字段全部暴露
    return JsonResponse(serializer.data, safe=False)
