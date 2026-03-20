const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/address-book', controller.addressPage);
router.post('/api/address', controller.createAddress);
router.delete('/api/address/:id', controller.deleteAddress);
router.get('/api/admin/export-address', controller.exportAddress);

module.exports = router;
