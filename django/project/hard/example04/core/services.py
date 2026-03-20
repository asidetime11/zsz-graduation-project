from django.core.cache import cache

from .models import CacheRecord, UserProfile


def get_sensitive_profile_data(user_id: int):
    cache_key = f"sensitive_profile:{user_id}"
    cached = cache.get(cache_key)
    if cached:
        return cached

    profile = UserProfile.objects.select_related("user", "org").filter(user_id=user_id).first()
    if not profile:
        return None

    payload = {
        "user_id": profile.user_id,
        "org_id": profile.org_id,
        "username": profile.user.username,
        "id_card": profile.id_card,
        "ssn": profile.ssn,
        "bank_account": profile.bank_account,
        "phone": profile.phone,
    }
    cache.set(cache_key, payload)
    CacheRecord.objects.create(cache_key=cache_key, cached_data=payload)
    return payload


def get_cached_hot_report(keyword: str):
    cache_key = "report:hot_users"
    cached = cache.get(cache_key)
    if cached:
        return cached

    rows = list(
        UserProfile.objects.filter(user__username__icontains=keyword)
        .values("org_id", "user_id", "id_card", "ssn", "bank_account", "phone")
        .order_by("-user_id")[:20]
    )
    cache.set(cache_key, rows)
    CacheRecord.objects.create(cache_key=cache_key, cached_data={"keyword": keyword, "rows": rows})
    return rows


def refresh_cache_without_ttl(user_id: int):
    payload = get_sensitive_profile_data(user_id)
    if payload:
        cache.set(f"sensitive_profile:{user_id}", payload)
        CacheRecord.objects.create(cache_key=f"sensitive_profile:{user_id}", cached_data=payload)
    return payload
