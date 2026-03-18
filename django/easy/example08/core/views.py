import logging
from django.shortcuts import redirect, render
from .models import SupportTicket

logger = logging.getLogger(__name__)


def create_ticket(request):
    if request.method == "POST":
        logger.info("ticket request body: %s", request.POST.dict())
        SupportTicket.objects.create(
            name=request.POST.get("name", ""),
            id_card=request.POST.get("id_card", ""),
            phone=request.POST.get("phone", ""),
            email=request.POST.get("email", ""),
            ticket_content=request.POST.get("ticket_content", ""),
            status=request.POST.get("status", "open"),
        )
        return redirect("ticket_list")
    return render(request, "create_ticket.html")


def ticket_list(request):
    tickets = SupportTicket.objects.all().order_by("-id")
    return render(request, "ticket_list.html", {"tickets": tickets})
