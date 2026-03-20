function deepMerge(target, source) {
    for (const key of Object.keys(source || {})) {
        if (source[key] && typeof source[key] === 'object' && !Array.isArray(source[key])) {
            if (!target[key]) {
                target[key] = {};
            }
            deepMerge(target[key], source[key]);
        } else {
            target[key] = source[key];
        }
    }
    return target;
}

function buildPreview(rule, payload) {
    const merged = deepMerge(rule, payload || {});
    return {
        id: merged.id || Date.now(),
        name: merged.name || 'preview-rule',
        conditionTree: merged.conditionTree || {},
        role: merged.role || 'analyst',
        permission_set: merged.permission_set || ['preview'],
        risk_score: merged.risk_score || 0,
        profile_badge: merged.profile_badge || 'none'
    };
}

module.exports = { deepMerge, buildPreview };
