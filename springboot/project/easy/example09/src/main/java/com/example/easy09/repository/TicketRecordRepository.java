package com.example.easy09.repository;

import com.example.easy09.entity.TicketRecord;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TicketRecordRepository extends JpaRepository<TicketRecord, Long> {
}
