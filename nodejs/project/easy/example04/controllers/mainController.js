const { addresses } = require('../models/dataStore');

function addressPage(req, res) {
    res.render('address_book', { addresses });
}

function createAddress(req, res) {
    addresses.push({
        id: addresses.length + 1,
        receiver_name: req.body.receiver_name || '',
        receiver_phone: req.body.receiver_phone || '',
        full_address: req.body.full_address || '',
        address_label_note: req.body.address_label_note || '',
        created_at: new Date().toISOString()
    });
    res.redirect('/address-book');
}

function deleteAddress(req, res) {
    res.json({ deleted: true, id: req.params.id });
}

function exportAddress(req, res) {
    res.render('admin_export', { addresses });
}

module.exports = { addressPage, createAddress, deleteAddress, exportAddress };
