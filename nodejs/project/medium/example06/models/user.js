class User {
    static data = [
        { id: 1, username: 'alice' },
        { id: 2, username: 'bob' }
    ];

    static findById(id) {
        return this.data.find((u) => u.id === Number(id));
    }
}

module.exports = User;
