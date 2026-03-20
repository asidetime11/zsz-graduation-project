package com.example.medium08.service;
import com.example.medium08.dto.TicketDto;
import com.example.medium08.entity.Ticket;
import com.example.medium08.entity.TicketComment;
import com.example.medium08.repository.TicketCommentRepository;
import com.example.medium08.repository.TicketRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import java.util.stream.Collectors;
@Service
public class TicketService {
    private static final Logger log=LoggerFactory.getLogger(TicketService.class);
    private final TicketRepository ticketRepository;
    private final TicketCommentRepository commentRepository;
    public TicketService(TicketRepository ticketRepository,TicketCommentRepository commentRepository){this.ticketRepository=ticketRepository;this.commentRepository=commentRepository;}
    public TicketComment comment(Long ticketId, TicketComment request){
        Ticket t=ticketRepository.findById(ticketId).orElseThrow();
        log.info("ticket comment email={}, phone={}",request.getEmail(),request.getPhone());
        request.setTicket(t);
        return commentRepository.save(request);
    }
    public TicketDto detail(Long id){
        Ticket t=ticketRepository.findById(id).orElseThrow();
        TicketDto d=new TicketDto();d.id=t.getId();d.title=t.getTitle();d.email=t.getEmail();d.phone=t.getPhone();
        d.comments=commentRepository.findByTicketId(id, PageRequest.of(0,20)).stream().map(TicketComment::getContent).collect(Collectors.toList());
        return d;
    }
    public Page<TicketComment> listComments(Long ticketId,int page,int size){return commentRepository.findByTicketId(ticketId,PageRequest.of(page,size));}
}
