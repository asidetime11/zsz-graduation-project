const store = require('../models/dataStore');

function revoke(userId) {
    const row = store.consents.find((x) => x.userId === userId) || store.consents[0];
    row.consent_status = 'revoked';
    row.revoke_time = Date.now();
    return row;
}

function enqueueProcessing(userId) {
    const job = { id: `job-${Date.now()}`, processing_job_id: `job-${Date.now()}`, userId, state: 'running' };
    store.jobs.push(job);
    return job;
}

module.exports = { revoke, enqueueProcessing };
