package com.example.easy04.entity;

import jakarta.persistence.*;

@Entity
public class ResumeCandidate {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String idCard;
    private String phone;
    private String email;
    private String maritalStatus;
    private String fertilityPlan;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getMaritalStatus() { return maritalStatus; }
    public void setMaritalStatus(String maritalStatus) { this.maritalStatus = maritalStatus; }
    public String getFertilityPlan() { return fertilityPlan; }
    public void setFertilityPlan(String fertilityPlan) { this.fertilityPlan = fertilityPlan; }
}
