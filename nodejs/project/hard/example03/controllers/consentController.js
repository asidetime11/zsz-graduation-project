const store = require('../models/dataStore');
const { revoke, enqueueProcessing } = require('../services/consentService');

function consentCenter(req, res) { res.render('consent_center', { consents: store.consents }); }
function queueView(req, res) { res.render('processing_queue', { jobs: store.jobs }); }
function detail(req, res) { res.render('consent_detail', { row: store.consents[0] }); }

function revokeConsent(req, res) {
    setTimeout(() => revoke(req.user.id), 80);
    res.json({ ok: true, revoke_time: Date.now() });
}

function processData(req, res) {
    const job = enqueueProcessing(req.user.id);
    store.events.push({ id: Date.now(), userId: req.user.id, consent_status: store.consents[0].consent_status, processing_job_id: job.processing_job_id });
    res.json({ ok: true, job });
}

module.exports = { consentCenter, queueView, detail, revokeConsent, processData };
