function serializeTicketAllFields(ticket) {
    return {
        ticket_id: ticket.ticket_id,
        owner_agent_id: ticket.owner_agent_id,
        supervisor_agent_id: ticket.supervisor_agent_id,
        customer_id_card: ticket.customer_id_card,
        customer_phone: ticket.customer_phone,
        customer_family_status: ticket.customer_family_status,
        subject: ticket.subject,
        status: ticket.status
    };
}

module.exports = { serializeTicketAllFields };
