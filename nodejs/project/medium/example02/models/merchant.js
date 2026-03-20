class Merchant {
    static data = [
        {
            id: 1,
            merchant_name: 'Blue Market',
            legal_person_id: '330102198805070033',
            bank_account: '6222020202020202',
            office_decoration_level: 'A'
        },
        {
            id: 2,
            merchant_name: 'Red Shop',
            legal_person_id: '440102198910100055',
            bank_account: '6223030303030303',
            office_decoration_level: 'B'
        }
    ];

    static findAll() {
        return this.data;
    }

    static findById(id) {
        return this.data.find((m) => m.id === Number(id));
    }
}

module.exports = Merchant;
