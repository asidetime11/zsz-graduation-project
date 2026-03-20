const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();
router.get('/events/signup', controller.signupPage);
router.post('/api/events/signup', controller.signupEvent);
router.get('/api/events/signups', controller.signupList);

module.exports = router;
