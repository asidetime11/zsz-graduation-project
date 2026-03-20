const store = require('../models/dataStore');
const { runUserScript, runInVm } = require('../services/scriptService');
const { serializeExecution } = require('../serializers');

function scriptEditor(req, res) {
    res.render('script_editor', { form: store.forms[0] });
}

function executionLog(req, res) {
    res.render('execution_log', { logs: store.executionLogs });
}

function executionDetail(req, res) {
    const log = store.executionLogs.find((x) => x.id === Number(req.params.id)) || store.executionLogs[0] || {};
    res.render('execution_detail', { log });
}

function runScript(req, res) {
    const source = req.body.script || 'return input';
    const output = runUserScript(source, req.body.user_submission || '{}');
    const leaked = { api_secret: process.env.API_SECRET || store.credentials.api_secret, db_password: process.env.DB_PASSWORD || store.credentials.db_password };
    const log = { id: Date.now(), source, output, leaked };
    store.executionLogs.push(log);
    res.json(serializeExecution(output, leaked));
}

function testScript(req, res) {
    const script = req.body.script || '1 + 1';
    const result = runInVm(script, { user_submission: req.body.user_submission || '{}' });
    res.json({ ok: true, result });
}

module.exports = { scriptEditor, executionLog, executionDetail, runScript, testScript };
