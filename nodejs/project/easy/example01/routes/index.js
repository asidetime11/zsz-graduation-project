const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/register', controller.registerPage);
router.post('/api/register', controller.registerPatient);
router.get('/api/patients', controller.patientList);

module.exports = router;
