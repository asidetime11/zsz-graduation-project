package com.example.easy02.repository;

import com.example.easy02.entity.EventApplicant;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EventApplicantRepository extends JpaRepository<EventApplicant, Long> {
}
