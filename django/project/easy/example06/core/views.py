from django.db import connection
from django.shortcuts import redirect, render
from .models import BorrowRecord


def search(request):
    keyword = request.GET.get("keyword", "")
    query = f"SELECT id,name,id_card,phone,book_title,borrow_date,return_date,created_at FROM core_borrowrecord WHERE book_title LIKE '%{keyword}%'"
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    return render(request, "search.html", {"rows": rows})


def borrow(request):
    if request.method == "POST":
        BorrowRecord.objects.create(
            name=request.POST.get("name", ""),
            id_card=request.POST.get("id_card", ""),
            phone=request.POST.get("phone", ""),
            book_title=request.POST.get("book_title", ""),
            borrow_date=request.POST.get("borrow_date") or None,
            return_date=request.POST.get("return_date") or None,
        )
        return redirect("search")
    return render(request, "borrow.html")
