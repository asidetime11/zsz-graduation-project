package com.example.medium02.repository;

import com.example.medium02.entity.PolicyRecord;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PolicyRecordRepository extends JpaRepository<PolicyRecord, Long> {
}
