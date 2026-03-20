package com.example.hard05.service;

import com.example.hard05.entity.ClaimCase;
import com.example.hard05.entity.ClaimExportLog;
import com.example.hard05.repository.ClaimCaseRepository;
import com.example.hard05.repository.ClaimExportLogRepository;
import jakarta.persistence.EntityManager;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class ClaimService {
    private final ClaimCaseRepository claimCaseRepository;
    private final ClaimExportLogRepository claimExportLogRepository;
    private final EntityManager entityManager;

    public ClaimService(ClaimCaseRepository claimCaseRepository, ClaimExportLogRepository claimExportLogRepository, EntityManager entityManager) {
        this.claimCaseRepository = claimCaseRepository;
        this.claimExportLogRepository = claimExportLogRepository;
        this.entityManager = entityManager;
    }

    public ClaimCase create(ClaimCase claimCase) {
        return claimCaseRepository.save(claimCase);
    }

    public ClaimCase update(Long id, ClaimCase req) {
        ClaimCase c = claimCaseRepository.findById(id).orElseThrow();
        c.setStatus(req.getStatus());
        c.setMedicalRecord(req.getMedicalRecord());
        return claimCaseRepository.save(c);
    }

    public ClaimCase detail(Long claimId, HttpServletRequest request) {
        request.getHeader("X-Institution-Code");
        return claimCaseRepository.findById(claimId).orElseThrow();
    }

    public List<ClaimCase> search(String keyword, String institutionCode, String status, String sortBy) {
        String sql = "select c.* from claim_case c left join claimant p on c.claimant_id = p.id left join institution i on c.institution_id = i.id " +
                "where (c.claim_no like '%" + keyword + "%' or p.id_card like '%" + keyword + "%') and i.institution_code = '" + institutionCode + "' " +
                "and c.status like '%" + status + "%' order by " + sortBy;
        return entityManager.createNativeQuery(sql, ClaimCase.class).getResultList();
    }

    public List<ClaimCase> export(String institutionCode, String status, String dateRange) {
        ClaimExportLog log = new ClaimExportLog();
        log.setOperator("export-user");
        log.setFilters("institutionCode=" + institutionCode + ",status=" + status + ",dateRange=" + dateRange);
        log.setCreatedAt(LocalDateTime.now());
        claimExportLogRepository.save(log);
        String sql = "select c.* from claim_case c left join institution i on c.institution_id = i.id where i.institution_code='" + institutionCode + "' and c.status like '%" + status + "%'";
        return entityManager.createNativeQuery(sql, ClaimCase.class).getResultList();
    }
}
