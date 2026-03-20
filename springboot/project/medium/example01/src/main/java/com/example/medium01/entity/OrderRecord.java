package com.example.medium01.entity;

import jakarta.persistence.*;

@Entity
public class OrderRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.EAGER)
    private AppUser user;

    private String itemName;
    private String idCard;
    private String phone;
    private String paymentCard;
    private String address;
    private String secondaryContact;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public AppUser getUser() { return user; }
    public void setUser(AppUser user) { this.user = user; }
    public String getItemName() { return itemName; }
    public void setItemName(String itemName) { this.itemName = itemName; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getPaymentCard() { return paymentCard; }
    public void setPaymentCard(String paymentCard) { this.paymentCard = paymentCard; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public String getSecondaryContact() { return secondaryContact; }
    public void setSecondaryContact(String secondaryContact) { this.secondaryContact = secondaryContact; }
}
