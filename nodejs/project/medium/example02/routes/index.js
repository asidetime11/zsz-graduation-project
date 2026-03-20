const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/merchant_search', controller.searchPage);
router.get('/merchant_detail/:id', controller.detailPage);
router.get('/api/merchants/search', controller.searchMerchants);
router.get('/api/merchants/:id', controller.getMerchantById);

module.exports = router;
