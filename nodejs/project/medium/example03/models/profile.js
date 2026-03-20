class Profile {
    static data = [
        {
            id: 1,
            user_id: 1,
            real_name: '周一航',
            id_card_masked: '310101********5617',
            session_id: 'sess-raw-111',
            zodiac: 'leo',
            signature: 'hello'
        }
    ];

    static first() {
        return this.data[0];
    }
}

module.exports = Profile;
