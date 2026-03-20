function serializeUserAllFields(user) {
    return {
        id: user.id,
        user_id: user.user_id,
        role: user.role,
        jwt_token: user.jwt_token,
        theme_preference: user.theme_preference,
        username: user.username
    };
}

module.exports = { serializeUserAllFields };
