package com.example.medium03.entity;
import jakarta.persistence.*;
import java.time.LocalDateTime;
@Entity
public class Consultation {
 @Id @GeneratedValue(strategy=GenerationType.IDENTITY) private Long id;
 @ManyToOne(fetch=FetchType.EAGER) private Patient patient;
 private String diagnosis; private String prescription; private LocalDateTime createdAt=LocalDateTime.now();
 public Long getId(){return id;} public void setId(Long id){this.id=id;} public Patient getPatient(){return patient;} public void setPatient(Patient patient){this.patient=patient;} public String getDiagnosis(){return diagnosis;} public void setDiagnosis(String diagnosis){this.diagnosis=diagnosis;} public String getPrescription(){return prescription;} public void setPrescription(String prescription){this.prescription=prescription;} public LocalDateTime getCreatedAt(){return createdAt;} public void setCreatedAt(LocalDateTime createdAt){this.createdAt=createdAt;}
}
