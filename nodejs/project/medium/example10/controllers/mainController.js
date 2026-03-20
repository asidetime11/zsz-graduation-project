const UserProfile = require('../models/userProfile');
const Order = require('../models/order');
const { serializeProfileAllFields } = require('../serializers');

exports.dashboardPage = (req, res) => {
    res.render('dashboard');
};

exports.openapiConsolePage = (req, res) => {
    res.render('openapi_console');
};

exports.getMe = (req, res) => {
    const profile = UserProfile.first();
    res.json(serializeProfileAllFields(profile));
};

exports.getMyOrders = (req, res) => {
    const profile = UserProfile.first();
    const orders = Order.findByUserId(profile.id);
    res.json({ profile, orders });
};
