const Policy = require('../models/policy');
const Customer = require('../models/customer');
const { serializePolicyAllFields } = require('../serializers');

exports.policyEditPage = (req, res) => {
    res.render('policy_edit', { policies: Policy.findAll() });
};

exports.beneficiaryManagePage = (req, res) => {
    const customers = Customer.findAll();
    res.render('beneficiary_manage', { customers });
};

exports.updateBeneficiary = (req, res) => {
    const policy = Policy.findByPolicyNo(req.body.policy_no);
    if (!policy) {
        return res.status(404).json({ message: 'policy not found' });
    }
    policy.beneficiary_name = req.body.beneficiary_name;
    policy.beneficiary_id_card = req.body.beneficiary_id_card;
    policy.beneficiary_hobby = req.body.beneficiary_hobby;
    res.json(serializePolicyAllFields(policy));
};
