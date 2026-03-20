package com.example.medium02.entity;

import jakarta.persistence.*;

@Entity
public class PolicyApplicant {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String idCard;
    private String bankAccount;
    private String medicalHistory;
    private String religion;
    private String familyGeneticTags;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getBankAccount() { return bankAccount; }
    public void setBankAccount(String bankAccount) { this.bankAccount = bankAccount; }
    public String getMedicalHistory() { return medicalHistory; }
    public void setMedicalHistory(String medicalHistory) { this.medicalHistory = medicalHistory; }
    public String getReligion() { return religion; }
    public void setReligion(String religion) { this.religion = religion; }
    public String getFamilyGeneticTags() { return familyGeneticTags; }
    public void setFamilyGeneticTags(String familyGeneticTags) { this.familyGeneticTags = familyGeneticTags; }
}
