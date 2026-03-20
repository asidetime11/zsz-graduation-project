package com.example.hard03.entity;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class CreditApplicant {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String idCard;
    private String socialAccount;
    @OneToMany(mappedBy = "applicant")
    private List<CreditCase> cases = new ArrayList<>();
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getSocialAccount() { return socialAccount; }
    public void setSocialAccount(String socialAccount) { this.socialAccount = socialAccount; }
}
