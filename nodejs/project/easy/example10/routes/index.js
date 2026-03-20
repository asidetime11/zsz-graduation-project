const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/points-center', controller.pointsPage);
router.get('/partner-sync', controller.partnerSyncPage);
router.post('/api/points/bind', controller.bindPoints);
router.post('/api/partner/push-profile', controller.pushProfile);

module.exports = router;
