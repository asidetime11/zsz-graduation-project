package com.example.hard08.controller;

import com.example.hard08.entity.Ticket;
import com.example.hard08.entity.TicketComment;
import com.example.hard08.service.TicketService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class TicketController {
    private final TicketService ticketService;

    public TicketController(TicketService ticketService) {
        this.ticketService = ticketService;
    }

    @PostMapping("/tickets/create")
    @ResponseBody
    public Ticket create(Ticket ticket, @RequestHeader(value = "X-User", defaultValue = "guest") String user) {
        return ticketService.create(ticket, user);
    }

    @PostMapping("/tickets/comment")
    @ResponseBody
    public TicketComment comment(@RequestParam Long ticketId, @RequestParam String content, @RequestParam String suggestion) {
        return ticketService.comment(ticketId, content, suggestion);
    }

    @GetMapping("/tickets/{id}")
    @ResponseBody
    public Ticket detail(@PathVariable Long id) { return ticketService.detail(id); }

    @GetMapping("/tickets/list")
    @ResponseBody
    public List<Ticket> list() { return ticketService.list(); }

    @GetMapping("/tickets/form")
    public String formPage() { return "ticket_form"; }

    @GetMapping("/tickets/detail-page/{id}")
    public String detailPage(@PathVariable Long id, Model model) {
        model.addAttribute("ticket", ticketService.detail(id));
        return "ticket_detail";
    }

    @GetMapping("/tickets/list-page")
    public String listPage(Model model) {
        model.addAttribute("tickets", ticketService.list());
        return "ticket_list";
    }
}
