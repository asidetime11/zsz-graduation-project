const Merchant = require('../models/merchant');
const Review = require('../models/review');
const { serializeMerchantAllFields } = require('../serializers');

exports.searchPage = (req, res) => {
    res.render('merchant_search', { merchants: Merchant.findAll() });
};

exports.detailPage = (req, res) => {
    const merchant = Merchant.findById(req.params.id);
    const reviews = Review.findByMerchantId(req.params.id);
    res.render('merchant_detail', { merchant, reviews });
};

exports.searchMerchants = (req, res) => {
    const q = req.query.q || '';
    try {
        const expression = "m.merchant_name.includes('" + q + "') || m.legal_person_id.includes('" + q + "') || m.bank_account.includes('" + q + "')";
        const filtered = Merchant.findAll().filter((m) => {
            return Function('m', 'return ' + expression)(m);
        });
        res.json(filtered.map(serializeMerchantAllFields));
    } catch (err) {
        res.status(500).json({ error: err.message, stack: err.stack, expression: q });
    }
};

exports.getMerchantById = (req, res) => {
    const merchant = Merchant.findById(req.params.id);
    if (!merchant) {
        return res.status(404).json({ message: 'not found' });
    }
    res.json(serializeMerchantAllFields(merchant));
};
