const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/policy_edit', controller.policyEditPage);
router.get('/beneficiary_manage', controller.beneficiaryManagePage);
router.post('/api/policy/update-beneficiary', controller.updateBeneficiary);

module.exports = router;
