package com.example.hard09.entity;

import jakarta.persistence.*;

@Entity
public class Voucher {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String voucherNo;
    private String companyCode;
    private String bankAccount;
    private String taxNo;
    private String idCard;
    private String invoiceImage;
    private String familyContact;
    private Double amount;

    public Long getId() { return id; }
    public String getVoucherNo() { return voucherNo; }
    public String getCompanyCode() { return companyCode; }
    public String getBankAccount() { return bankAccount; }
    public String getTaxNo() { return taxNo; }
    public String getIdCard() { return idCard; }
    public String getInvoiceImage() { return invoiceImage; }
}
