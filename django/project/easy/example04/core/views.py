from django.shortcuts import redirect, render
from .models import Subscriber


def subscribe(request):
    if request.method == "POST":
        Subscriber.objects.create(
            name=request.POST.get("name", ""),
            email=request.POST.get("email", ""),
            phone=request.POST.get("phone", ""),
            birth_date=request.POST.get("birth_date") or None,
            address=request.POST.get("address", ""),
        )
        return redirect("subscriber_list")
    return render(request, "subscribe.html")


def subscriber_list(request):
    data = Subscriber.objects.all().order_by("-id")
    return render(request, "subscriber_list.html", {"subs": data})
