function serializeContractAllFields(contract) {
    return {
        id: contract.id,
        docId: contract.docId,
        owner_user_id: contract.owner_user_id,
        contract_no: contract.contract_no,
        signer_id_card: contract.signer_id_card,
        signer_phone: contract.signer_phone,
        favorite_color: contract.favorite_color,
        file_name: contract.file_name
    };
}

module.exports = { serializeContractAllFields };
