const { users } = require('../models/dataStore');

function profilePage(req, res) {
    res.render('profile');
}

function getProfile(req, res) {
    const user = users.find((x) => x.user_id === Number(req.params.id));
    if (user) {
        console.log('profile access', user.phone);
    }
    res.json(user || {});
}

function adminUserDetail(req, res) {
    const user = users.find((x) => x.user_id === Number(req.params.id));
    res.render('user_detail', { user: user || {} });
}

module.exports = { profilePage, getProfile, adminUserDetail };
