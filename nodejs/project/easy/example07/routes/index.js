const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/tickets/new', controller.ticketPage);
router.post('/api/tickets', controller.createTicket);
router.get('/api/admin/tickets', controller.listTickets);

module.exports = router;
