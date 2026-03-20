package com.example.easy09.entity;

import jakarta.persistence.*;

@Entity
public class TicketRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String subject;
    private String idCard;
    private String phone;
    private String address;
    private String familyAddress;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getSubject() { return subject; }
    public void setSubject(String subject) { this.subject = subject; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public String getFamilyAddress() { return familyAddress; }
    public void setFamilyAddress(String familyAddress) { this.familyAddress = familyAddress; }
}
