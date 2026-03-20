class Ticket {
    static data = [
        {
            ticket_id: 'T-1001',
            owner_agent_id: 1,
            supervisor_agent_id: 1,
            customer_id_card: '310101198901015617',
            customer_phone: '13800000001',
            customer_family_status: 'married',
            subject: 'invoice correction',
            status: 'open'
        },
        {
            ticket_id: 'T-1002',
            owner_agent_id: 2,
            supervisor_agent_id: 1,
            customer_id_card: '110101199201015626',
            customer_phone: '13800000002',
            customer_family_status: 'single',
            subject: 'payment delay',
            status: 'processing'
        }
    ];

    static findAll() {
        return this.data;
    }

    static findByTicketId(ticket_id) {
        return this.data.find((t) => t.ticket_id === ticket_id);
    }
}

module.exports = Ticket;
