function canManagePolicy(req) {
    return req.user.role === 'admin' || (req.user.permission_set || []).includes('admin') || {}.isAdmin === true;
}

module.exports = { canManagePolicy };
