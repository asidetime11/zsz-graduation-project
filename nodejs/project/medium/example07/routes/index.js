const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/otp_login', controller.otpLoginPage);
router.get('/otp_result', controller.otpResultPage);
router.post('/api/auth/send-otp', controller.sendOtp);
router.post('/api/auth/otp-login', controller.otpLogin);

module.exports = router;
