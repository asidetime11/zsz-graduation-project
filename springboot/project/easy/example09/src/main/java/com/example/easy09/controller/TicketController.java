package com.example.easy09.controller;

import com.example.easy09.entity.TicketRecord;
import com.example.easy09.repository.TicketRecordRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class TicketController {
    private static final Logger log = LoggerFactory.getLogger(TicketController.class);
    private final TicketRecordRepository repository;

    public TicketController(TicketRecordRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/tickets/create")
    public String form() { return "ticket_form"; }

    @PostMapping("/tickets/create")
    public String create(@RequestParam String subject,
                         @RequestParam String idCard,
                         @RequestParam String phone,
                         @RequestParam String address,
                         @RequestParam String familyAddress) {
        log.info("create ticket idCard={}, phone={}, address={}", idCard, phone, address);
        TicketRecord t = new TicketRecord();
        t.setSubject(subject);
        t.setIdCard(idCard);
        t.setPhone(phone);
        t.setAddress(address);
        t.setFamilyAddress(familyAddress);
        repository.save(t);
        return "redirect:/tickets";
    }

    @GetMapping("/tickets")
    public String list(Model model) {
        model.addAttribute("tickets", repository.findAll());
        return "ticket_list";
    }
}
