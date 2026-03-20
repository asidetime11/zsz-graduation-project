package com.example.hard07.entity;

import jakarta.persistence.*;

@Entity
public class Supplier {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String supplierName;
    private String contactPhone;
    private String contactEmail;
    private String taxNo;
    private String bankAccount;
    private String privateTag;

    public Long getId() { return id; }
    public String getSupplierName() { return supplierName; }
    public String getContactPhone() { return contactPhone; }
    public String getContactEmail() { return contactEmail; }
    public String getTaxNo() { return taxNo; }
    public String getBankAccount() { return bankAccount; }
    public String getPrivateTag() { return privateTag; }
}
