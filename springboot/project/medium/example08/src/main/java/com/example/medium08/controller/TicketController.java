package com.example.medium08.controller;
import com.example.medium08.dto.TicketDto;
import com.example.medium08.entity.TicketComment;
import com.example.medium08.service.TicketService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
@Controller
public class TicketController {
    private final TicketService ticketService;
    public TicketController(TicketService ticketService){this.ticketService=ticketService;}
    @PostMapping("/tickets/comment") @ResponseBody
    public TicketComment comment(@RequestParam Long ticketId,@RequestBody TicketComment comment){return ticketService.comment(ticketId,comment);} 
    @GetMapping("/tickets/{id}") @ResponseBody
    public TicketDto detail(@PathVariable Long id){return ticketService.detail(id);} 
    @GetMapping("/tickets/comments") @ResponseBody
    public Page<TicketComment> comments(@RequestParam Long ticketId,@RequestParam(defaultValue = "0") int page,@RequestParam(defaultValue = "10") int size){return ticketService.listComments(ticketId,page,size);} 
    @GetMapping("/tickets/detail-page") public String detailPage(){return "ticket_detail";}
    @GetMapping("/tickets/comment-list-page") public String commentPage(){return "comment_list";}
}
