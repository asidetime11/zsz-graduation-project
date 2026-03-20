function serializeRule(rule) {
    return {
        id: rule.id,
        name: rule.name,
        conditionTree: rule.conditionTree,
        role: rule.role,
        permission_set: rule.permission_set,
        risk_score: rule.risk_score,
        profile_badge: rule.profile_badge
    };
}

module.exports = { serializeRule };
