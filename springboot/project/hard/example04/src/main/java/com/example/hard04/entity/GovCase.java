package com.example.hard04.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
public class GovCase {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String caseNo;
    private String caseType;
    private String status;
    private LocalDateTime closedAt;
    @ManyToOne
    private CitizenProfile citizenProfile;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getCaseNo() { return caseNo; }
    public void setCaseNo(String caseNo) { this.caseNo = caseNo; }
    public String getCaseType() { return caseType; }
    public void setCaseType(String caseType) { this.caseType = caseType; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public LocalDateTime getClosedAt() { return closedAt; }
    public void setClosedAt(LocalDateTime closedAt) { this.closedAt = closedAt; }
    public CitizenProfile getCitizenProfile() { return citizenProfile; }
    public void setCitizenProfile(CitizenProfile citizenProfile) { this.citizenProfile = citizenProfile; }
}
