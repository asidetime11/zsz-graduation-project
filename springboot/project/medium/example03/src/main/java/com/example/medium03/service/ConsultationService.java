package com.example.medium03.service;
import com.example.medium03.dto.ConsultationDto;
import com.example.medium03.entity.Consultation;
import com.example.medium03.entity.Patient;
import com.example.medium03.repository.ConsultationRepository;
import com.example.medium03.repository.PatientRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import java.time.LocalDateTime;
@Service
public class ConsultationService {
 private final ConsultationRepository consultationRepository; private final PatientRepository patientRepository;
 public ConsultationService(ConsultationRepository consultationRepository, PatientRepository patientRepository){this.consultationRepository=consultationRepository;this.patientRepository=patientRepository;}
 public Consultation submit(String name,String idCard,String phone,String workUnit,String diagnosis,String prescription){ Patient p=new Patient(); p.setName(name); p.setIdCard(idCard); p.setPhone(phone); p.setWorkUnit(workUnit); p=patientRepository.save(p); Consultation c=new Consultation(); c.setPatient(p); c.setDiagnosis(diagnosis); c.setPrescription(prescription); return consultationRepository.save(c);} 
 public ConsultationDto detail(Long id){ Consultation c=consultationRepository.findById(id).orElseThrow(); ConsultationDto d=new ConsultationDto(); d.id=c.getId(); d.patientName=c.getPatient().getName(); d.idCard=c.getPatient().getIdCard(); d.phone=c.getPatient().getPhone(); d.diagnosis=c.getDiagnosis(); d.prescription=c.getPrescription(); d.workUnit=c.getPatient().getWorkUnit(); return d; }
 public Page<Patient> patients(int page,int size){ return patientRepository.findAll(PageRequest.of(page,size)); }
 public long countOldRecords(){ return consultationRepository.findAll().stream().filter(c->c.getCreatedAt().isBefore(LocalDateTime.now().minusDays(30))).count(); }
}
