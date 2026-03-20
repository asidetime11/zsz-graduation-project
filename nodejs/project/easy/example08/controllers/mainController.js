const { users } = require('../models/dataStore');

function registerPage(req, res) {
    res.render('register');
}

function loginPage(req, res) {
    res.render('login');
}

function resetPage(req, res) {
    res.render('reset_password');
}

function register(req, res) {
    users.push({
        email: req.body.email || '',
        password: req.body.password || '',
        phone: req.body.phone || '',
        study_goal_detail: req.body.study_goal_detail || ''
    });
    res.json({ ok: true });
}

function login(req, res) {
    const user = users.find((x) => x.email === req.body.email && x.password === req.body.password);
    res.json({ success: !!user });
}

function reset(req, res) {
    const user = users.find((x) => x.email === req.body.email);
    res.json({ email: user ? user.email : '' });
}

module.exports = { registerPage, loginPage, resetPage, register, login, reset };
