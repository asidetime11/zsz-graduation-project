const { tickets, serviceLogs } = require('../models/dataStore');

function ticketPage(req, res) {
    res.render('ticket_create');
}

function createTicket(req, res) {
    const ticket = {
        name: req.body.name || '',
        phone: req.body.phone || '',
        address: req.body.address || '',
        id_card_images: req.body.id_card_images || '',
        household_register_city: req.body.household_register_city || '',
        created_at: new Date().toISOString()
    };
    serviceLogs.push(`ticket ${ticket.name} ${ticket.phone} ${ticket.address}`);
    tickets.push(ticket);
    res.json({ ok: true });
}

function listTickets(req, res) {
    res.render('ticket_list', { tickets, serviceLogs });
}

module.exports = { ticketPage, createTicket, listTickets };
