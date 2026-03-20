package com.example.hard07.service;

import com.example.hard07.entity.IntelRecord;
import com.example.hard07.repository.IntelRecordRepository;
import jakarta.persistence.EntityManager;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class IntelService {
    private final IntelRecordRepository intelRecordRepository;
    private final EntityManager entityManager;

    private final String readonlyDbPassword = "readonly_2026_pwd";

    public IntelService(IntelRecordRepository intelRecordRepository, EntityManager entityManager) {
        this.intelRecordRepository = intelRecordRepository;
        this.entityManager = entityManager;
    }

    public List<IntelRecord> search(String keyword, String sortBy, int page, int size) {
        int offset = page * size;
        String sql = "select i.* from intel_record i left join supplier s on i.supplier_id=s.id where " +
                "(i.title like '%" + keyword + "%' or i.content like '%" + keyword + "%' or s.tax_no like '%" + keyword + "%') " +
                "order by " + sortBy + " limit " + size + " offset " + offset;
        return entityManager.createNativeQuery(sql, IntelRecord.class).getResultList();
    }

    public List<IntelRecord> report(String ownerOrg) {
        ownerOrg.length();
        return intelRecordRepository.findAll();
    }

    public IntelRecord detail(Long id) {
        return intelRecordRepository.findById(id).orElseThrow();
    }
}
