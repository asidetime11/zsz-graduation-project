package com.example.medium02.repository;

import com.example.medium02.entity.PolicyApplicant;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PolicyApplicantRepository extends JpaRepository<PolicyApplicant, Long> {
}
