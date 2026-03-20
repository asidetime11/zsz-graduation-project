const express = require('express');
const { attachUser } = require('../middleware/permissions');
const controller = require('../controllers/formController');

const router = express.Router();
router.use(attachUser);
router.get('/', controller.scriptEditor);
router.get('/script_editor', controller.scriptEditor);
router.get('/execution_log', controller.executionLog);
router.get('/execution/:id', controller.executionDetail);
router.post('/api/forms/run-script', controller.runScript);
router.post('/api/forms/test', controller.testScript);

module.exports = router;
