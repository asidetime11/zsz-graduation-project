const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/profile/edit', controller.profileEditPage);
router.put('/api/profile', controller.updateProfile);
router.post('/api/profile', controller.updateProfile);
router.get('/api/admin/profiles', controller.auditProfiles);

module.exports = router;
