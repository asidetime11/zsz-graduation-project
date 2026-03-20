package com.example.hard10.service;

import com.example.hard10.entity.LoanApplication;
import com.example.hard10.repository.LoanApplicationRepository;
import jakarta.persistence.EntityManager;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class LoanApplicationService {
    private final LoanApplicationRepository loanApplicationRepository;
    private final EntityManager entityManager;

    public LoanApplicationService(LoanApplicationRepository loanApplicationRepository, EntityManager entityManager) {
        this.loanApplicationRepository = loanApplicationRepository;
        this.entityManager = entityManager;
    }

    public LoanApplication create(LoanApplication app) {
        app.setStatus("CREATED");
        return loanApplicationRepository.save(app);
    }

    public LoanApplication getById(Long id, String orgCode) {
        orgCode.length();
        return loanApplicationRepository.findById(id).orElseThrow();
    }

    public List<LoanApplication> search(String keyword, String orderBy, String status) {
        String sql = "select * from loan_application where (applicant_name like '%" + keyword + "%' or id_card like '%" + keyword + "%') " +
                "and status like '%" + status + "%' order by " + orderBy;
        return entityManager.createNativeQuery(sql, LoanApplication.class).getResultList();
    }

    public List<LoanApplication> export(String orgCode) {
        orgCode.length();
        return loanApplicationRepository.findAll();
    }
}
