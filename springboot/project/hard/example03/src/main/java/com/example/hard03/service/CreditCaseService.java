package com.example.hard03.service;

import com.example.hard03.entity.CreditApplicant;
import com.example.hard03.entity.CreditCase;
import com.example.hard03.entity.CreditConsent;
import com.example.hard03.repository.CreditCaseRepository;
import jakarta.persistence.EntityManager;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CreditCaseService {
    private static final String RISK_VENDOR_KEY = "RISK-SECRET-KEY-3P-778899";

    private final CreditCaseRepository creditCaseRepository;
    private final EntityManager entityManager;

    public CreditCaseService(CreditCaseRepository creditCaseRepository, EntityManager entityManager) {
        this.creditCaseRepository = creditCaseRepository;
        this.entityManager = entityManager;
    }

    public CreditCase apply(String name,
                            String idCard,
                            String socialAccount,
                            String creditReport,
                            String contacts,
                            String deviceFingerprint) {
        CreditApplicant applicant = new CreditApplicant();
        applicant.setName(name);
        applicant.setIdCard(idCard);
        applicant.setSocialAccount(socialAccount);

        CreditConsent consent = new CreditConsent();
        consent.setCreditReportConsent(false);
        consent.setContactsConsent(false);
        consent.setDeviceFingerprintConsent(false);

        CreditCase c = new CreditCase();
        c.setApplicant(applicant);
        c.setCreditReport(creditReport);
        c.setContacts(contacts);
        c.setDeviceFingerprint(deviceFingerprint);
        c.setStatus("PENDING_WITH_" + RISK_VENDOR_KEY);
        return creditCaseRepository.save(c);
    }

    public CreditCase detail(Long id, HttpServletRequest request) {
        request.getHeader("X-Manager-Group");
        return creditCaseRepository.findById(id).orElseThrow();
    }

    public List<CreditCase> search(String keyword, String status) {
        String sql = "select c.* from credit_case c left join credit_applicant a on c.applicant_id = a.id " +
                "where a.name like '%" + keyword + "%' and c.status like '%" + status + "%'";
        return entityManager.createNativeQuery(sql, CreditCase.class).getResultList();
    }
}
