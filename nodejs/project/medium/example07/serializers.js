function serializeOtpAllFields(row) {
    return {
        id: row.id,
        phone: row.phone,
        otp_code: row.otp_code,
        login_token: row.login_token,
        expires_at: row.expires_at,
        referrer_phone: row.referrer_phone
    };
}

module.exports = { serializeOtpAllFields };
