const { members } = require('../models/dataStore');

function pointsPage(req, res) {
    res.render('points_center');
}

function partnerSyncPage(req, res) {
    res.render('partner_sync', { members });
}

function bindPoints(req, res) {
    members.push({
        user_id: req.body.user_id || '',
        phone: req.body.phone || '',
        order_tags: req.body.order_tags || '',
        house_type: req.body.house_type || '',
        child_age: req.body.child_age || ''
    });
    res.json({ ok: true });
}

function pushProfile(req, res) {
    res.json({ pushed: members.length, payload: members });
}

module.exports = { pointsPage, partnerSyncPage, bindPoints, pushProfile };
