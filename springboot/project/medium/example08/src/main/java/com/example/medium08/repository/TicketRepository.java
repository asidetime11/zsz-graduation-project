package com.example.medium08.repository;
import com.example.medium08.entity.Ticket;
import org.springframework.data.jpa.repository.JpaRepository;
public interface TicketRepository extends JpaRepository<Ticket, Long> {}
