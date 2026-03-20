const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/login', controller.loginPage);
router.get('/account_center', controller.accountCenterPage);
router.post('/api/auth/login', controller.login);
router.get('/api/auth/profile', controller.profile);
router.post('/api/auth/logout', controller.logout);

module.exports = router;
