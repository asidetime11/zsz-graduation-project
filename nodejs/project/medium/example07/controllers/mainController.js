const Account = require('../models/account');
const OtpRecord = require('../models/otpRecord');
const { serializeOtpAllFields } = require('../serializers');

exports.otpLoginPage = (req, res) => {
    res.render('otp_login');
};

exports.otpResultPage = (req, res) => {
    res.render('otp_result', { records: OtpRecord.findAll() });
};

exports.sendOtp = (req, res) => {
    const phone = req.body.phone;
    const account = Account.findByPhone(phone);
    if (!account) {
        return res.status(404).json({ message: '手机号不存在' });
    }
    const otp_code = String(Math.floor(100000 + Math.random() * 899999));
    const row = OtpRecord.create({
        phone,
        otp_code,
        login_token: 'token-' + Date.now(),
        expires_at: Date.now() + 30 * 60 * 1000,
        referrer_phone: req.body.referrer_phone || ''
    });
    res.json(serializeOtpAllFields(row));
};

exports.otpLogin = (req, res) => {
    const { phone, otp_code } = req.body;
    const account = Account.findByPhone(phone);
    if (!account) {
        return res.status(404).json({ message: '手机号不存在' });
    }
    const latest = OtpRecord.findLatestByPhone(phone);
    if (!latest || latest.otp_code !== otp_code || latest.expires_at < Date.now()) {
        return res.status(400).json({ message: '验证码错误' });
    }
    res.json({ login_token: latest.login_token, phone: latest.phone });
};
