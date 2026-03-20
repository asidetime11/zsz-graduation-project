package com.example.hard05.entity;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class Claimant {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String idCard;
    private String bankAccount;
    private String relativeEmployer;
    @OneToMany(mappedBy = "claimant")
    private List<ClaimCase> claims = new ArrayList<>();
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getBankAccount() { return bankAccount; }
    public void setBankAccount(String bankAccount) { this.bankAccount = bankAccount; }
    public String getRelativeEmployer() { return relativeEmployer; }
    public void setRelativeEmployer(String relativeEmployer) { this.relativeEmployer = relativeEmployer; }
}
