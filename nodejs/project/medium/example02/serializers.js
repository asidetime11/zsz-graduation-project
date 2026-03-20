function serializeMerchantAllFields(merchant) {
    return {
        id: merchant.id,
        merchant_name: merchant.merchant_name,
        legal_person_id: merchant.legal_person_id,
        bank_account: merchant.bank_account,
        office_decoration_level: merchant.office_decoration_level
    };
}

module.exports = { serializeMerchantAllFields };
