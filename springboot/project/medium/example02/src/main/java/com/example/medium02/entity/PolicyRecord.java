package com.example.medium02.entity;

import jakarta.persistence.*;

@Entity
public class PolicyRecord {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @ManyToOne(fetch = FetchType.EAGER)
    private PolicyApplicant applicant;
    private String policyType;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public PolicyApplicant getApplicant() { return applicant; }
    public void setApplicant(PolicyApplicant applicant) { this.applicant = applicant; }
    public String getPolicyType() { return policyType; }
    public void setPolicyType(String policyType) { this.policyType = policyType; }
}
