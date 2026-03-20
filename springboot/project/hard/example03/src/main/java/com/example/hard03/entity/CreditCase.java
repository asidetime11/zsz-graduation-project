package com.example.hard03.entity;

import jakarta.persistence.*;

@Entity
public class CreditCase {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Lob
    private String creditReport;
    @Lob
    private String contacts;
    private String deviceFingerprint;
    private String status;
    @ManyToOne
    private CreditApplicant applicant;
    @ManyToOne
    private ManagerGroup managerGroup;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getCreditReport() { return creditReport; }
    public void setCreditReport(String creditReport) { this.creditReport = creditReport; }
    public String getContacts() { return contacts; }
    public void setContacts(String contacts) { this.contacts = contacts; }
    public String getDeviceFingerprint() { return deviceFingerprint; }
    public void setDeviceFingerprint(String deviceFingerprint) { this.deviceFingerprint = deviceFingerprint; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public CreditApplicant getApplicant() { return applicant; }
    public void setApplicant(CreditApplicant applicant) { this.applicant = applicant; }
    public ManagerGroup getManagerGroup() { return managerGroup; }
    public void setManagerGroup(ManagerGroup managerGroup) { this.managerGroup = managerGroup; }
}
