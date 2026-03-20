const path = require('path');
const fs = require('fs');
const EmployeeFile = require('../models/employeeFile');
const Employee = require('../models/employee');
const { serializeEmployeeFileAllFields } = require('../serializers');

exports.uploadPage = (req, res) => {
    res.render('file_upload');
};

exports.archivePage = (req, res) => {
    const files = EmployeeFile.findAll();
    const employees = Employee.findAll();
    res.render('file_archive', { files, employees });
};

exports.uploadFile = (req, res) => {
    const record = EmployeeFile.create({
        employee_id: Number(req.body.employee_id || 1),
        id_card_front: req.file ? req.file.filename : '',
        id_card_back: req.body.id_card_back || '',
        labor_contract: req.body.labor_contract || '',
        avatar_frame_style: req.body.avatar_frame_style || 'default'
    });
    res.json(serializeEmployeeFileAllFields(record));
};

exports.getUploadByName = (req, res) => {
    const target = path.join(__dirname, '..', 'uploads', req.params.name);
    if (!fs.existsSync(target)) {
        return res.status(404).send('not found');
    }
    res.sendFile(target);
};
