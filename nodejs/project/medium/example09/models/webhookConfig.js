class WebhookConfig {
    static data = [
        {
            id: 1,
            callback_url: 'http://127.0.0.1:8080/callback',
            access_token: 'seed-access-token',
            order_id: 'ORD-1001',
            callback_alias: 'default'
        }
    ];

    static create(row) {
        const next = { id: this.data.length + 1, ...row };
        this.data.push(next);
        return next;
    }

    static findLatest() {
        return this.data.slice(-1)[0];
    }

    static findAll() {
        return this.data;
    }
}

module.exports = WebhookConfig;
