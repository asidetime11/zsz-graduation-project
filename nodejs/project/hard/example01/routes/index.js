const express = require('express');
const controller = require('../controllers/ruleController');

const router = express.Router();

router.get('/', controller.renderBuilder);
router.get('/rule_builder', controller.renderBuilder);
router.get('/admin_policy', controller.renderAdmin);
router.get('/rules/:id', controller.renderDetail);
router.post('/api/rules/preview', controller.previewRule);
router.post('/api/rules/save', controller.saveRule);

module.exports = router;
