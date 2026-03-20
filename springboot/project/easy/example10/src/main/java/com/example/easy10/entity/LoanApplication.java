package com.example.easy10.entity;

import jakarta.persistence.*;

@Entity
public class LoanApplication {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String applicantName;
    private String idCard;
    private String bankCard;
    private String incomeProof;
    private String relativeContact;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getApplicantName() { return applicantName; }
    public void setApplicantName(String applicantName) { this.applicantName = applicantName; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getBankCard() { return bankCard; }
    public void setBankCard(String bankCard) { this.bankCard = bankCard; }
    public String getIncomeProof() { return incomeProof; }
    public void setIncomeProof(String incomeProof) { this.incomeProof = incomeProof; }
    public String getRelativeContact() { return relativeContact; }
    public void setRelativeContact(String relativeContact) { this.relativeContact = relativeContact; }
}
