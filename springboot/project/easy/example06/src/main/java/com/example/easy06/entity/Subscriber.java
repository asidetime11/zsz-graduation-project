package com.example.easy06.entity;

import jakarta.persistence.*;

@Entity
public class Subscriber {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String phone;
    private String address;
    private String hobbyTags;
    private Boolean marketingConsent;
    private Boolean canceled;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public String getHobbyTags() { return hobbyTags; }
    public void setHobbyTags(String hobbyTags) { this.hobbyTags = hobbyTags; }
    public Boolean getMarketingConsent() { return marketingConsent; }
    public void setMarketingConsent(Boolean marketingConsent) { this.marketingConsent = marketingConsent; }
    public Boolean getCanceled() { return canceled; }
    public void setCanceled(Boolean canceled) { this.canceled = canceled; }
}
