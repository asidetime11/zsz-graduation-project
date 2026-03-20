const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/contacts', controller.contactsPage);
router.get('/api/contacts', controller.getContacts);
router.get('/api/contacts/export', controller.exportContacts);
router.get('/export-history', controller.exportHistoryPage);

module.exports = router;
