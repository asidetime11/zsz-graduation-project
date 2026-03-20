const state = {
    rules: [
        {
            id: 1,
            name: 'KYC high risk',
            conditionTree: { score: { $gt: 80 } },
            role: 'analyst',
            permission_set: ['preview'],
            risk_score: 84,
            profile_badge: 'gold'
        }
    ],
    policyLogs: [
        { id: 11, ruleId: 1, action: 'create', operator: 'u-101' }
    ],
    users: [
        { id: 'u-101', role: 'analyst', permission_set: ['preview'] },
        { id: 'u-001', role: 'admin', permission_set: ['preview', 'save', 'admin'] }
    ],
    audits: []
};

module.exports = state;
