const { signups } = require('../models/dataStore');

function signupPage(req, res) {
    res.render('signup');
}

function signupEvent(req, res) {
    signups.push({
        student_id: req.body.student_id || '',
        phone: req.body.phone || '',
        emergency_phone: req.body.emergency_phone || '',
        parent_company: req.body.parent_company || '',
        created_at: new Date().toISOString()
    });
    res.redirect('/api/events/signups');
}

function signupList(req, res) {
    res.render('signup_admin', { signups });
}

module.exports = { signupPage, signupEvent, signupList };
