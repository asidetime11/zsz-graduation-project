package com.example.hard05.entity;

import jakarta.persistence.*;

@Entity
public class ClaimCase {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String claimNo;
    @Lob
    private String medicalRecord;
    private String status;

    @ManyToOne
    private Institution institution;

    @ManyToOne
    private Claimant claimant;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getClaimNo() { return claimNo; }
    public void setClaimNo(String claimNo) { this.claimNo = claimNo; }
    public String getMedicalRecord() { return medicalRecord; }
    public void setMedicalRecord(String medicalRecord) { this.medicalRecord = medicalRecord; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public Institution getInstitution() { return institution; }
    public void setInstitution(Institution institution) { this.institution = institution; }
    public Claimant getClaimant() { return claimant; }
    public void setClaimant(Claimant claimant) { this.claimant = claimant; }
}
