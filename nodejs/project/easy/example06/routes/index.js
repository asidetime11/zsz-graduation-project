const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/profile', controller.profilePage);
router.get('/api/profile/:id', controller.getProfile);
router.get('/api/admin/user/:id', controller.adminUserDetail);

module.exports = router;
