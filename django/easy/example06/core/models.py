from django.db import models


class BorrowRecord(models.Model):
    name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    book_title = models.CharField(max_length=200)
    borrow_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
