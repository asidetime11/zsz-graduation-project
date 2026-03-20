package com.example.hard03.entity;

import jakarta.persistence.*;

@Entity
public class CreditConsent {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long applicantId;
    private boolean creditReportConsent;
    private boolean contactsConsent;
    private boolean deviceFingerprintConsent;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Long getApplicantId() { return applicantId; }
    public void setApplicantId(Long applicantId) { this.applicantId = applicantId; }
    public boolean isCreditReportConsent() { return creditReportConsent; }
    public void setCreditReportConsent(boolean creditReportConsent) { this.creditReportConsent = creditReportConsent; }
    public boolean isContactsConsent() { return contactsConsent; }
    public void setContactsConsent(boolean contactsConsent) { this.contactsConsent = contactsConsent; }
    public boolean isDeviceFingerprintConsent() { return deviceFingerprintConsent; }
    public void setDeviceFingerprintConsent(boolean deviceFingerprintConsent) { this.deviceFingerprintConsent = deviceFingerprintConsent; }
}
