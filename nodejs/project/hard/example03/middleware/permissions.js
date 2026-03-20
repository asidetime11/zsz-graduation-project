function withUser(req, res, next) { req.user = { id: req.headers['x-user-id'] || 'u301' }; next(); }
module.exports = { withUser };
