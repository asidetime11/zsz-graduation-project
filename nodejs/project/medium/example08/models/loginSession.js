class LoginSession {
    static data = [];

    static create(row) {
        const next = { id: this.data.length + 1, ...row };
        this.data.push(next);
        return next;
    }

    static findAll() {
        return this.data;
    }
}

module.exports = LoginSession;
