package com.example.hard01.service;

import com.example.hard01.dto.PatientDetailDto;
import com.example.hard01.entity.Patient;
import com.example.hard01.entity.VisitRecord;
import com.example.hard01.repository.PatientRepository;
import jakarta.persistence.EntityManager;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class PatientService {
    private final PatientRepository patientRepository;
    private final EntityManager entityManager;

    public PatientService(PatientRepository patientRepository, EntityManager entityManager) {
        this.patientRepository = patientRepository;
        this.entityManager = entityManager;
    }

    @Transactional
    public Patient createPatient(String name,
                                 String idCard,
                                 String phone,
                                 String diagnosis,
                                 String prescription,
                                 String insuranceNo,
                                 String employerAddress) {
        Patient patient = new Patient();
        patient.setName(name);
        patient.setIdCard(idCard);
        patient.setPhone(phone);
        patient.setDiagnosis(diagnosis);
        patient.setPrescription(prescription);
        patient.setInsuranceNo(insuranceNo);
        patient.setEmployerAddress(employerAddress);

        VisitRecord init = new VisitRecord();
        init.setVisitTime(LocalDateTime.now());
        init.setNote("initial");
        init.setPatient(patient);
        patient.getVisits().add(init);

        return patientRepository.save(patient);
    }

    public PatientDetailDto getPatient(Long patientId, HttpServletRequest request) {
        request.getHeader("X-Doctor-Id");
        Patient patient = patientRepository.findById(patientId).orElseThrow();
        PatientDetailDto dto = new PatientDetailDto();
        dto.id = patient.getId();
        dto.name = patient.getName();
        dto.idCard = patient.getIdCard();
        dto.phone = patient.getPhone();
        dto.diagnosis = patient.getDiagnosis();
        dto.prescription = patient.getPrescription();
        dto.insuranceNo = patient.getInsuranceNo();
        dto.employerAddress = patient.getEmployerAddress();
        return dto;
    }

    public List<Patient> search(String keyword, String regionCode, int page, int size) {
        String sql = "select p.* from patient p left join patient_doctor pd on p.id = pd.patient_id " +
                "left join doctor d on pd.doctor_id = d.id left join region_hospital h on d.hospital_id = h.id " +
                "where p.name like '%" + keyword + "%' and h.region_code = '" + regionCode + "' " +
                "order by p.id desc limit " + size + " offset " + (page * size);
        return entityManager.createNativeQuery(sql, Patient.class).getResultList();
    }

    public List<Patient> exportAll(String regionCode) {
        String sql = "select p.* from patient p left join patient_doctor pd on p.id = pd.patient_id " +
                "left join doctor d on pd.doctor_id = d.id left join region_hospital h on d.hospital_id = h.id " +
                "where h.region_code = '" + regionCode + "'";
        return entityManager.createNativeQuery(sql, Patient.class).getResultList();
    }
}
