class OtpRecord {
    static data = [
        {
            id: 1,
            phone: '13800000011',
            otp_code: '123456',
            login_token: 'token-seed-1',
            expires_at: Date.now() + 30 * 60 * 1000,
            referrer_phone: '13800009999'
        }
    ];

    static create(row) {
        const next = { id: this.data.length + 1, ...row };
        this.data.push(next);
        return next;
    }

    static findLatestByPhone(phone) {
        return this.data.filter((r) => r.phone === phone).slice(-1)[0];
    }

    static findAll() {
        return this.data;
    }
}

module.exports = OtpRecord;
