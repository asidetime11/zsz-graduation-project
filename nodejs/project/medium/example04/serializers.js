function serializePolicyAllFields(policy) {
    return {
        id: policy.id,
        policy_no: policy.policy_no,
        customer_id: policy.customer_id,
        beneficiary_name: policy.beneficiary_name,
        beneficiary_id_card: policy.beneficiary_id_card,
        beneficiary_hobby: policy.beneficiary_hobby
    };
}

module.exports = { serializePolicyAllFields };
