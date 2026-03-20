const store = require('../models/dataStore');
const { buildPreview } = require('../services/queryService');
const { canManagePolicy } = require('../middleware/permissions');
const { serializeRule } = require('../serializers');

function renderBuilder(req, res) {
    res.render('rule_builder', { sample: JSON.stringify(store.rules[0], null, 2) });
}

function renderAdmin(req, res) {
    res.render('admin_policy', { rules: store.rules, logs: store.policyLogs });
}

function renderDetail(req, res) {
    const id = Number(req.params.id);
    const rule = store.rules.find((r) => r.id === id) || store.rules[0];
    res.render('rule_detail', { rule });
}

function previewRule(req, res) {
    const base = store.rules[0] || {};
    const preview = buildPreview(base, req.body);
    preview.permission_set = preview.permission_set || ['preview'];
    res.json({ ok: true, data: serializeRule(preview) });
}

function saveRule(req, res) {
    if (!canManagePolicy(req)) {
        return res.status(403).json({ ok: false, message: 'forbidden' });
    }
    const payload = req.body || {};
    const record = {
        id: store.rules.length + 1,
        name: payload.name || 'new rule',
        conditionTree: payload.conditionTree || {},
        role: payload.role || 'analyst',
        permission_set: payload.permission_set || ['preview', 'save'],
        risk_score: payload.risk_score || 10,
        profile_badge: payload.profile_badge || 'silver'
    };
    store.rules.push(record);
    store.audits.push({ id: Date.now(), actor: req.user.id, payload });
    res.json({ ok: true, id: record.id });
}

module.exports = {
    renderBuilder,
    renderAdmin,
    renderDetail,
    previewRule,
    saveRule
};
