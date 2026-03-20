class UserProfile {
    static data = [
        {
            id: 1,
            profile: 'VIP-User-Group-A',
            email: 'vip.user@example.com',
            phone: '13812340000',
            api_key_masked: 'ak_live_xxx999',
            ui_layout_choice: 'wide'
        }
    ];

    static first() {
        return this.data[0];
    }
}

module.exports = UserProfile;
