class Agent {
    static data = [
        { id: 1, name: 'Lina', role: 'supervisor', team: 'A' },
        { id: 2, name: 'Mark', role: 'agent', team: 'A' }
    ];

    static findAll() {
        return this.data;
    }

    static findById(id) {
        return this.data.find((a) => a.id === Number(id));
    }
}

module.exports = Agent;
