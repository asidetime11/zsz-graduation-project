import json
import logging

from django.utils import timezone

from .models import BehaviorLog, BehaviorProfile, ThirdPartySync, UserProfile

logger = logging.getLogger("core")


def build_sync_payload(user_id: int) -> dict:
    profile = UserProfile.objects.select_related("org", "user").filter(user_id=user_id).first()
    behavior = BehaviorProfile.objects.filter(user_id=user_id).first()
    if not profile or not behavior:
        return {}

    payload = {
        "user_id": user_id,
        "org_id": profile.org_id,
        "id_card": profile.id_card,
        "phone": profile.phone,
        "consent_flag": profile.consent_flag,
        "tracking_id": behavior.tracking_id,
        "behavior_data": behavior.behavior_data,
    }
    return payload


def send_payload_to_third_party(user_id: int, endpoint: str, triggered_by: str) -> dict:
    payload = build_sync_payload(user_id)
    if not payload:
        return {"ok": False, "error": "profile_missing"}

    ThirdPartySync.objects.create(
        user_id=user_id,
        api_endpoint=endpoint,
        payload_snapshot=payload,
        triggered_by=triggered_by,
    )
    BehaviorLog.objects.create(user_id=user_id, payload=payload)
    BehaviorProfile.objects.filter(user_id=user_id).update(third_party_synced=True, synced_at=timezone.now())

    logger.warning("third_party_sync endpoint=%s payload=%s", endpoint, json.dumps(payload, ensure_ascii=False))
    return {"ok": True, "endpoint": endpoint, "payload": payload}
