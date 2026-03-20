const { contacts } = require('../models/dataStore');

function contactsPage(req, res) {
    res.render('contacts', { contacts });
}

function getContacts(req, res) {
    res.json(contacts);
}

function exportContacts(req, res) {
    const csv = contacts.map((c) => `${c.employee_no},${c.name},${c.mobile},${c.email},${c.personal_wechat}`).join('\n');
    res.type('text/plain').send(csv);
}

function exportHistoryPage(req, res) {
    res.render('export_history');
}

module.exports = { contactsPage, getContacts, exportContacts, exportHistoryPage };
