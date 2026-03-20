const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/ticket_assign', controller.ticketAssignPage);
router.get('/ticket_detail/:id', controller.ticketDetailPage);
router.get('/api/tickets/:id', controller.getTicket);
router.patch('/api/tickets/:id/assign', controller.assignTicket);

module.exports = router;
