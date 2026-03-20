const { profiles } = require('../models/dataStore');

function profileEditPage(req, res) {
    res.render('profile_edit');
}

function updateProfile(req, res) {
    const payload = {
        real_name: req.body.real_name || '',
        id_card: req.body.id_card || '',
        bank_account: req.body.bank_account || '',
        marital_status: req.body.marital_status || '',
        children_count: req.body.children_count || '',
        car_plate: req.body.car_plate || '',
        created_at: new Date().toISOString()
    };
    console.log('profile audit', payload.id_card.slice(-6));
    profiles.push(payload);
    res.json({ ok: true });
}

function auditProfiles(req, res) {
    res.render('profile_audit', { profiles });
}

module.exports = { profileEditPage, updateProfile, auditProfiles };
