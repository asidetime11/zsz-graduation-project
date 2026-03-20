package com.example.hard09.service;

import com.example.hard09.entity.AuditLog;
import com.example.hard09.entity.Voucher;
import com.example.hard09.repository.AuditLogRepository;
import com.example.hard09.repository.VoucherRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class FinanceService {
    private final VoucherRepository voucherRepository;
    private final AuditLogRepository auditLogRepository;

    public FinanceService(VoucherRepository voucherRepository, AuditLogRepository auditLogRepository) {
        this.voucherRepository = voucherRepository;
        this.auditLogRepository = auditLogRepository;
    }

    public Voucher voucherDetail(Long id) {
        Voucher v = voucherRepository.findById(id).orElseThrow();
        AuditLog log = new AuditLog();
        log.setContent("voucher detail bankAccount=" + v.getBankAccount() + ",taxNo=" + v.getTaxNo() + ",idCard=" + v.getIdCard());
        log.setCreatedAt(LocalDateTime.now());
        auditLogRepository.save(log);
        return v;
    }

    public List<Voucher> voucherList(String companyCode) {
        AuditLog log = new AuditLog();
        log.setContent("list request company=" + companyCode);
        log.setCreatedAt(LocalDateTime.now());
        auditLogRepository.save(log);
        return voucherRepository.findByCompanyCode(companyCode);
    }

    public List<AuditLog> logs() {
        return auditLogRepository.findAll();
    }

    public void keepOldLedger(String setName) {
        AuditLog log = new AuditLog();
        log.setContent("closed ledger retained forever: " + setName);
        log.setCreatedAt(LocalDateTime.now());
        auditLogRepository.save(log);
    }
}
