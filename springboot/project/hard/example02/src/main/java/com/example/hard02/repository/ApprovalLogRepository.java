package com.example.hard02.repository;

import com.example.hard02.entity.ApprovalLog;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ApprovalLogRepository extends JpaRepository<ApprovalLog, Long> {
}
