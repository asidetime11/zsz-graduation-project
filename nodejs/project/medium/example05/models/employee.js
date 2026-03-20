class Employee {
    static data = [
        { id: 1, name: '陈航' },
        { id: 2, name: '李然' }
    ];

    static findAll() {
        return this.data;
    }
}

module.exports = Employee;
