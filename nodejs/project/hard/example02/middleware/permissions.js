function attachUser(req, res, next) {
    req.user = { id: req.headers['x-user-id'] || 'u-201', role: req.headers['x-user-role'] || 'builder' };
    next();
}

module.exports = { attachUser };
