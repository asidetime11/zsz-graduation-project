class Account {
    static data = [
        { id: 1, phone: '13800000011', name: '赵云', referrer_phone: '13800009999' },
        { id: 2, phone: '13800000012', name: '钱阳', referrer_phone: '' }
    ];

    static findByPhone(phone) {
        return this.data.find((a) => a.phone === phone);
    }
}

module.exports = Account;
