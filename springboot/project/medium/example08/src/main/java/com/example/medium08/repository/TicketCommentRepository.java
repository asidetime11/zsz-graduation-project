package com.example.medium08.repository;
import com.example.medium08.entity.TicketComment;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
public interface TicketCommentRepository extends JpaRepository<TicketComment, Long> {
    Page<TicketComment> findByTicketId(Long ticketId, Pageable pageable);
}
