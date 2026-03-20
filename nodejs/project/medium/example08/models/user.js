class User {
    static data = [
        {
            id: 1,
            user_id: 'U-1001',
            role: 'admin',
            jwt_token: '',
            theme_preference: 'dark',
            username: 'root-admin'
        }
    ];

    static findById(id) {
        return this.data.find((u) => u.id === Number(id));
    }

    static findByUserId(user_id) {
        return this.data.find((u) => u.user_id === user_id);
    }
}

module.exports = User;
