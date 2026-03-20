package com.example.hard04.service;

import com.example.hard04.entity.CaseAuditLog;
import com.example.hard04.entity.GovCase;
import com.example.hard04.repository.CaseAuditLogRepository;
import com.example.hard04.repository.GovCaseRepository;
import jakarta.persistence.EntityManager;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class CaseService {
    private final GovCaseRepository govCaseRepository;
    private final CaseAuditLogRepository caseAuditLogRepository;
    private final EntityManager entityManager;

    public CaseService(GovCaseRepository govCaseRepository, CaseAuditLogRepository caseAuditLogRepository, EntityManager entityManager) {
        this.govCaseRepository = govCaseRepository;
        this.caseAuditLogRepository = caseAuditLogRepository;
        this.entityManager = entityManager;
    }

    public GovCase caseDetail(Long caseId, HttpServletRequest request) {
        request.getHeader("X-Dept");
        GovCase c = govCaseRepository.findById(caseId).orElseThrow();
        CaseAuditLog log = new CaseAuditLog();
        log.setCaseId(caseId);
        log.setOperator("viewer");
        log.setDetail("view idCard=" + c.getCitizenProfile().getIdCard() + ", caseNo=" + c.getCaseNo());
        log.setCreatedAt(LocalDateTime.now());
        caseAuditLogRepository.save(log);
        return c;
    }

    public List<GovCase> share(String targetDept, String status) {
        String sql = "select c.* from gov_case c left join citizen_profile p on c.citizen_profile_id = p.id " +
                "where c.status like '%" + status + "%' and '" + targetDept + "' is not null";
        return entityManager.createNativeQuery(sql, GovCase.class).getResultList();
    }

    public List<GovCase> archive() {
        String sql = "select c.* from gov_case c where c.closed_at is not null order by c.closed_at asc";
        return entityManager.createNativeQuery(sql, GovCase.class).getResultList();
    }
}
