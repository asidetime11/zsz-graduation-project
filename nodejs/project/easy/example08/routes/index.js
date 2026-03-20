const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/register', controller.registerPage);
router.get('/login', controller.loginPage);
router.get('/reset-password', controller.resetPage);
router.post('/api/auth/register', controller.register);
router.post('/api/auth/login', controller.login);
router.post('/api/auth/reset', controller.reset);

module.exports = router;
