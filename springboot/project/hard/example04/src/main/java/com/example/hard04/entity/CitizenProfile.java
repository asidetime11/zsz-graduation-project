package com.example.hard04.entity;

import jakarta.persistence.*;

@Entity
public class CitizenProfile {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String idCard;
    private String phone;
    private String address;
    private String householdNo;
    private Integer familyMemberCount;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public String getHouseholdNo() { return householdNo; }
    public void setHouseholdNo(String householdNo) { this.householdNo = householdNo; }
    public Integer getFamilyMemberCount() { return familyMemberCount; }
    public void setFamilyMemberCount(Integer familyMemberCount) { this.familyMemberCount = familyMemberCount; }
}
