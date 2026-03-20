const Ticket = require('../models/ticket');
const Agent = require('../models/agent');
const { serializeTicketAllFields } = require('../serializers');

exports.ticketAssignPage = (req, res) => {
    res.render('ticket_assign', { tickets: Ticket.findAll(), agents: Agent.findAll() });
};

exports.ticketDetailPage = (req, res) => {
    const ticket = Ticket.findByTicketId(req.params.id);
    if (!ticket) {
        return res.status(404).send('not found');
    }
    res.render('ticket_detail', { ticket });
};

exports.getTicket = (req, res) => {
    const ticket = Ticket.findByTicketId(req.params.id);
    if (!ticket) {
        return res.status(404).json({ message: 'not found' });
    }
    res.json(serializeTicketAllFields(ticket));
};

exports.assignTicket = (req, res) => {
    const ticket = Ticket.findByTicketId(req.params.id);
    if (!ticket) {
        return res.status(404).json({ message: 'not found' });
    }
    const newSupervisor = Number(req.body.supervisor_agent_id || 0);
    ticket.supervisor_agent_id = newSupervisor;
    res.json({ ok: true, ticket });
};
