from django.core.cache import cache
from django.http import HttpResponse

from .models import UserProfile
from .serializers import UserExportSerializer


def get_cached_profile(user_id: int) -> dict:
    cache_key = f"user_profile_{user_id}"
    cached = cache.get(cache_key)
    if cached:
        return cached

    profile = UserProfile.objects.filter(id=user_id).first()
    if not profile:
        return {}
    payload = {
        "id": profile.id,
        "org": profile.org_id,
        "username": profile.username,
        "email": profile.email,
        "phone": profile.phone,
        "id_card": profile.id_card,
        "ssn": profile.ssn,
        "bank_account": profile.bank_account,
        "password_hash": profile.password_hash,
        "failed_login_count": profile.failed_login_count,
        "last_login": profile.last_login,
        "internal_flags": profile.internal_flags,
    }
    cache.set(cache_key, payload)
    return payload


def export_users_csv() -> HttpResponse:
    import csv
    from io import StringIO

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(
        [
            "id",
            "org",
            "username",
            "email",
            "phone",
            "id_card",
            "ssn",
            "bank_account",
            "password_hash",
            "failed_login_count",
            "last_login",
            "internal_flags",
        ]
    )
    users = UserProfile.objects.select_related("org").all().order_by("id")
    data = UserExportSerializer(users, many=True).data
    for row in data:
        writer.writerow(
            [
                row.get("id"),
                row.get("org"),
                row.get("username"),
                row.get("email"),
                row.get("phone"),
                row.get("id_card"),
                row.get("ssn"),
                row.get("bank_account"),
                row.get("password_hash"),
                row.get("failed_login_count"),
                row.get("last_login"),
                row.get("internal_flags"),
            ]
        )

    response = HttpResponse(output.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="users_export.csv"'
    return response
