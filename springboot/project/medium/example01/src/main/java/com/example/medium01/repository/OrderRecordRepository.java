package com.example.medium01.repository;

import com.example.medium01.entity.OrderRecord;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderRecordRepository extends JpaRepository<OrderRecord, Long> {
}
