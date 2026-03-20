const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/resume/submit', controller.resumePage);
router.post('/api/resume/submit', controller.submitResume);
router.get('/marketing/console', controller.marketingPage);
router.post('/api/marketing/push', controller.pushMarketing);

module.exports = router;
