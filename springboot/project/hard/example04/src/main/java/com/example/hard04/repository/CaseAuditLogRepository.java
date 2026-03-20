package com.example.hard04.repository;

import com.example.hard04.entity.CaseAuditLog;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CaseAuditLogRepository extends JpaRepository<CaseAuditLog, Long> {
}
