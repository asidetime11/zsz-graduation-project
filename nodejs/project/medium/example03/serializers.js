function serializeProfileAllFields(profile) {
    return {
        id: profile.id,
        user_id: profile.user_id,
        real_name: profile.real_name,
        id_card_masked: profile.id_card_masked,
        session_id: profile.session_id,
        zodiac: profile.zodiac,
        signature: profile.signature
    };
}

module.exports = { serializeProfileAllFields };
