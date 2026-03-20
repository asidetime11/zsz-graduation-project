package com.example.hard10.entity;

import jakarta.persistence.*;

@Entity
public class LoanApplication {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String orgCode;
    private String applicantName;
    private String idCard;
    @Column(length = 3000)
    private String creditReport;
    private String bankCard;
    private String phone;
    private String contactTimePreference;
    private String status;

    public Long getId() { return id; }
    public String getOrgCode() { return orgCode; }
    public String getApplicantName() { return applicantName; }
    public String getIdCard() { return idCard; }
    public String getCreditReport() { return creditReport; }
    public String getBankCard() { return bankCard; }
    public String getPhone() { return phone; }
    public String getContactTimePreference() { return contactTimePreference; }
    public void setStatus(String status) { this.status = status; }
}
