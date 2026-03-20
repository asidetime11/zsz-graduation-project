package com.example.medium10.repository;
import com.example.medium10.entity.LoanApplication;
import org.springframework.data.jpa.repository.JpaRepository;
public interface LoanApplicationRepository extends JpaRepository<LoanApplication, Long> {}
