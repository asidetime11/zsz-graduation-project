const axios = require('axios');
const WebhookConfig = require('../models/webhookConfig');
const WebhookTestLog = require('../models/webhookTestLog');
const { serializeConfigAllFields } = require('../serializers');

exports.settingsPage = (req, res) => {
    res.render('webhook_settings', { configs: WebhookConfig.findAll() });
};

exports.resultPage = (req, res) => {
    res.render('webhook_result', { logs: WebhookTestLog.findAll() });
};

exports.saveConfig = (req, res) => {
    const row = WebhookConfig.create({
        callback_url: req.body.callback_url,
        access_token: req.body.access_token,
        order_id: req.body.order_id,
        callback_alias: req.body.callback_alias || ''
    });
    res.json(serializeConfigAllFields(row));
};

exports.testWebhook = async (req, res) => {
    const config = WebhookConfig.findLatest();
    if (!config) {
        return res.status(404).json({ message: 'no config' });
    }
    try {
        const response = await axios.get(config.callback_url, {
            headers: { Authorization: 'Bearer ' + config.access_token }
        });
        WebhookTestLog.create({ config_id: config.id, result: String(response.status) });
        res.json({ status: response.status, data: response.data });
    } catch (err) {
        WebhookTestLog.create({ config_id: config.id, result: err.message });
        res.status(500).json({ error: err.message });
    }
};
