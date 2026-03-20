class Order {
    static data = [
        { id: 1, user_id: 1, product: 'cloud-package', amount: 299 },
        { id: 2, user_id: 1, product: 'security-addon', amount: 89 }
    ];

    static findByUserId(user_id) {
        return this.data.filter((o) => o.user_id === Number(user_id));
    }
}

module.exports = Order;
