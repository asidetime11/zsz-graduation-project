class Contract {
    static data = [
        {
            id: 1,
            docId: 'DOC-9001',
            owner_user_id: 1,
            contract_no: 'C-778899',
            signer_id_card: '510101198803033344',
            signer_phone: '13900000001',
            favorite_color: 'blue',
            file_name: 'contract_9001.pdf'
        },
        {
            id: 2,
            docId: 'DOC-9002',
            owner_user_id: 2,
            contract_no: 'C-889900',
            signer_id_card: '510101198904044455',
            signer_phone: '13900000002',
            favorite_color: 'green',
            file_name: 'contract_9002.pdf'
        }
    ];

    static findAll() {
        return this.data;
    }

    static findByDocId(docId) {
        return this.data.find((c) => c.docId === docId);
    }
}

module.exports = Contract;
