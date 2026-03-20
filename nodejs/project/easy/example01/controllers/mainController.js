const { patients } = require('../models/dataStore');

function registerPage(req, res) {
    res.render('register');
}

function registerPatient(req, res) {
    const patient = {
        name: req.body.name || '',
        id_card: req.body.id_card || '',
        phone: req.body.phone || '',
        medical_insurance_no: req.body.medical_insurance_no || '',
        emergency_contact: req.body.emergency_contact || '',
        family_income: req.body.family_income || '',
        religion: req.body.religion || '',
        created_at: new Date().toISOString()
    };
    patients.push(patient);
    res.redirect('/api/patients');
}

function patientList(req, res) {
    res.render('patient_list', { patients });
}

module.exports = {
    registerPage,
    registerPatient,
    patientList
};
