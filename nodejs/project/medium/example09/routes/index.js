const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/webhook_settings', controller.settingsPage);
router.get('/webhook_result', controller.resultPage);
router.post('/api/webhook/config', controller.saveConfig);
router.post('/api/webhook/test', controller.testWebhook);

module.exports = router;
