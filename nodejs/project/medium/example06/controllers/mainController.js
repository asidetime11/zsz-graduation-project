const Contract = require('../models/contract');
const User = require('../models/user');
const { serializeContractAllFields } = require('../serializers');

exports.contractListPage = (req, res) => {
    res.render('contract_list', { contracts: Contract.findAll() });
};

exports.contractPreviewPage = (req, res) => {
    const contract = Contract.findByDocId(req.params.docId);
    res.render('contract_preview', { contract });
};

exports.getContracts = (req, res) => {
    res.json(Contract.findAll().map(serializeContractAllFields));
};

exports.downloadContract = (req, res) => {
    const contract = Contract.findByDocId(req.params.docId);
    if (!contract) {
        return res.status(404).json({ message: 'not found' });
    }
    const owner = User.findById(contract.owner_user_id);
    res.json({
        file_name: contract.file_name,
        contract_no: contract.contract_no,
        signer_id_card: contract.signer_id_card,
        signer_phone: contract.signer_phone,
        owner
    });
};
