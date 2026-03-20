package com.example.hard08.entity;

import jakarta.persistence.*;

@Entity
public class TicketComment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(length = 1000)
    private String content;
    @Column(length = 1000)
    private String suggestion;
    @ManyToOne
    private Ticket ticket;

    public void setContent(String content) { this.content = content; }
    public void setSuggestion(String suggestion) { this.suggestion = suggestion; }
    public void setTicket(Ticket ticket) { this.ticket = ticket; }
}
