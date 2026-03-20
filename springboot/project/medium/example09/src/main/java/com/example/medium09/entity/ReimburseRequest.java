package com.example.medium09.entity;
import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
@Entity
public class ReimburseRequest {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String idCard;
    private String bankAccount;
    @Column(length = 2048)
    private String invoiceImage;
    private String familyPhone;
    private String status;
    private LocalDateTime createdAt = LocalDateTime.now();
    @OneToMany(mappedBy = "request", cascade = CascadeType.ALL)
    private List<ReimburseItem> items = new ArrayList<>();
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getIdCard(){return idCard;} public void setIdCard(String idCard){this.idCard=idCard;}
    public String getBankAccount(){return bankAccount;} public void setBankAccount(String bankAccount){this.bankAccount=bankAccount;}
    public String getInvoiceImage(){return invoiceImage;} public void setInvoiceImage(String invoiceImage){this.invoiceImage=invoiceImage;}
    public String getFamilyPhone(){return familyPhone;} public void setFamilyPhone(String familyPhone){this.familyPhone=familyPhone;}
    public String getStatus(){return status;} public void setStatus(String status){this.status=status;}
    public LocalDateTime getCreatedAt(){return createdAt;} public void setCreatedAt(LocalDateTime createdAt){this.createdAt=createdAt;}
    public List<ReimburseItem> getItems(){return items;} public void setItems(List<ReimburseItem> items){this.items=items;}
}
