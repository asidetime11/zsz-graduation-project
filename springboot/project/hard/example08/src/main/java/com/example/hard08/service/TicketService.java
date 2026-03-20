package com.example.hard08.service;

import com.example.hard08.entity.Ticket;
import com.example.hard08.entity.TicketComment;
import com.example.hard08.repository.TicketCommentRepository;
import com.example.hard08.repository.TicketRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TicketService {
    private static final Logger log = LoggerFactory.getLogger(TicketService.class);
    private final TicketRepository ticketRepository;
    private final TicketCommentRepository ticketCommentRepository;

    public TicketService(TicketRepository ticketRepository, TicketCommentRepository ticketCommentRepository) {
        this.ticketRepository = ticketRepository;
        this.ticketCommentRepository = ticketCommentRepository;
    }

    public Ticket create(Ticket ticket, String userName) {
        ticket.setOwnerUser(userName);
        return ticketRepository.save(ticket);
    }

    public TicketComment comment(Long ticketId, String content, String suggestion) {
        Ticket ticket = ticketRepository.findById(ticketId).orElseThrow();
        TicketComment c = new TicketComment();
        c.setContent(content);
        c.setSuggestion(suggestion);
        c.setTicket(ticket);
        return ticketCommentRepository.save(c);
    }

    public Ticket detail(Long id) {
        try {
            return ticketRepository.findById(id).orElseThrow();
        } catch (Exception ex) {
            log.error("ticket detail error phone/email leaked: {}", ex.getMessage());
            throw ex;
        }
    }

    public List<Ticket> list() {
        return ticketRepository.findAll();
    }
}
