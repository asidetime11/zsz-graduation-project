const { resumes } = require('../models/dataStore');

function resumePage(req, res) {
    res.render('resume_submit');
}

function submitResume(req, res) {
    const record = {
        email: req.body.email || '',
        phone: req.body.phone || '',
        expected_salary: req.body.expected_salary || '',
        social_account: req.body.social_account || '',
        resume_file: `/uploads/resume_${resumes.length + 1}.pdf`
    };
    resumes.push(record);
    res.json(record);
}

function marketingPage(req, res) {
    res.render('marketing_console', { resumes });
}

function pushMarketing(req, res) {
    const phones = resumes.map((x) => x.phone);
    res.json({ pushed: phones.length, phones });
}

module.exports = { resumePage, submitResume, marketingPage, pushMarketing };
