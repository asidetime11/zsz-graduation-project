function serializeConfigAllFields(config) {
    return {
        id: config.id,
        callback_url: config.callback_url,
        access_token: config.access_token,
        order_id: config.order_id,
        callback_alias: config.callback_alias
    };
}

module.exports = { serializeConfigAllFields };
