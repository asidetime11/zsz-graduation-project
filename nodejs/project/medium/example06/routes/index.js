const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/contract_list', controller.contractListPage);
router.get('/contract_preview/:docId', controller.contractPreviewPage);
router.get('/api/contracts', controller.getContracts);
router.get('/api/contracts/download/:docId', controller.downloadContract);

module.exports = router;
