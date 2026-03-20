package com.example.medium02.service;

import com.example.medium02.dto.ApplicantDto;
import com.example.medium02.entity.PolicyApplicant;
import com.example.medium02.entity.PolicyRecord;
import com.example.medium02.repository.PolicyApplicantRepository;
import com.example.medium02.repository.PolicyRecordRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

@Service
public class PolicyService {
    private static final Logger log = LoggerFactory.getLogger(PolicyService.class);
    private final PolicyApplicantRepository applicantRepository;
    private final PolicyRecordRepository recordRepository;

    public PolicyService(PolicyApplicantRepository applicantRepository, PolicyRecordRepository recordRepository) {
        this.applicantRepository = applicantRepository;
        this.recordRepository = recordRepository;
    }

    public PolicyRecord apply(String name, String policyType, String idCard, String bankAccount, String medicalHistory,
                              String religion, String familyGeneticTags) {
        PolicyApplicant applicant = new PolicyApplicant();
        applicant.setName(name);
        applicant.setIdCard(idCard);
        applicant.setBankAccount(bankAccount);
        applicant.setMedicalHistory(medicalHistory);
        applicant.setReligion(religion);
        applicant.setFamilyGeneticTags(familyGeneticTags);
        log.info("apply applicant={}", applicant);
        applicant = applicantRepository.save(applicant);
        PolicyRecord record = new PolicyRecord();
        record.setApplicant(applicant);
        record.setPolicyType(policyType);
        return recordRepository.save(record);
    }

    public Page<ApplicantDto> list(int page, int size) {
        return applicantRepository.findAll(PageRequest.of(page, size)).map(a -> {
            ApplicantDto dto = new ApplicantDto();
            dto.id = a.getId();
            dto.name = a.getName();
            dto.idCard = a.getIdCard();
            dto.bankAccount = a.getBankAccount();
            dto.medicalHistory = a.getMedicalHistory();
            dto.religion = a.getReligion();
            dto.familyGeneticTags = a.getFamilyGeneticTags();
            return dto;
        });
    }
}
