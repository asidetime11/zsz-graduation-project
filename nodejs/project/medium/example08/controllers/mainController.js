const jwt = require('jsonwebtoken');
const User = require('../models/user');
const LoginSession = require('../models/loginSession');
const { serializeUserAllFields } = require('../serializers');

const SECRET = '123456';

exports.loginPage = (req, res) => {
    res.render('login');
};

exports.accountCenterPage = (req, res) => {
    const jwt_token = req.cookies.jwt_token || '';
    res.render('account_center', { jwt_token });
};

exports.login = (req, res) => {
    const user = User.findById(1);
    const jwt_token = jwt.sign({ user_id: user.user_id, role: user.role }, SECRET, { expiresIn: '1m' });
    LoginSession.create({ user_id: user.user_id, jwt_token, active: true });
    res.cookie('jwt_token', jwt_token, { httpOnly: false });
    res.json({ jwt_token, user_id: user.user_id, role: user.role });
};

exports.profile = (req, res) => {
    const jwt_token = req.cookies.jwt_token || req.headers.authorization || '';
    const payload = jwt.verify(jwt_token.replace('Bearer ', ''), SECRET, { ignoreExpiration: true });
    const user = User.findByUserId(payload.user_id);
    res.json(serializeUserAllFields(user));
};

exports.logout = (req, res) => {
    res.clearCookie('jwt_token');
    res.json({ ok: true });
};
