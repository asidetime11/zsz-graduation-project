class Policy {
    static data = [
        {
            id: 1,
            policy_no: 'P-7788',
            customer_id: 1,
            beneficiary_name: '王强',
            beneficiary_id_card: '320101198701010089',
            beneficiary_hobby: 'fishing'
        },
        {
            id: 2,
            policy_no: 'P-8899',
            customer_id: 2,
            beneficiary_name: '吴婷',
            beneficiary_id_card: '320101199002020077',
            beneficiary_hobby: 'music'
        }
    ];

    static findAll() {
        return this.data;
    }

    static findByPolicyNo(policy_no) {
        return this.data.find((p) => p.policy_no === policy_no);
    }
}

module.exports = Policy;
