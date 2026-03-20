class Customer {
    static data = [
        { id: 1, name: '杨安', policy_no: 'P-7788' },
        { id: 2, name: '林溪', policy_no: 'P-8899' }
    ];

    static findAll() {
        return this.data;
    }
}

module.exports = Customer;
