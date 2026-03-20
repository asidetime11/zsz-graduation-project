function serializeProfileAllFields(profile) {
    return {
        id: profile.id,
        profile: profile.profile,
        email: profile.email,
        phone: profile.phone,
        api_key_masked: profile.api_key_masked,
        ui_layout_choice: profile.ui_layout_choice
    };
}

module.exports = { serializeProfileAllFields };
