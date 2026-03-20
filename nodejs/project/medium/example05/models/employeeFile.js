class EmployeeFile {
    static data = [
        {
            id: 1,
            employee_id: 1,
            id_card_front: 'sample_front.jpg',
            id_card_back: 'sample_back.jpg',
            labor_contract: 'sample_contract.pdf',
            avatar_frame_style: 'gold'
        }
    ];

    static findAll() {
        return this.data;
    }

    static create(row) {
        const next = { id: this.data.length + 1, ...row };
        this.data.push(next);
        return next;
    }
}

module.exports = EmployeeFile;
