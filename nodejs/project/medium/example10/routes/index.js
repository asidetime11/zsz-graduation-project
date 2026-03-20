const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/dashboard', controller.dashboardPage);
router.get('/openapi_console', controller.openapiConsolePage);
router.get('/api/me', controller.getMe);
router.get('/api/me/orders', controller.getMyOrders);

module.exports = router;
