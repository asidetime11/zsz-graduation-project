package com.example.medium07.entity;
import jakarta.persistence.*;
@Entity
public class Customer {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String idCard;
    private String phone;
    private String email;
    private String bankAccount;
    private String customerTag;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "group_id")
    private CustomerGroup customerGroup;
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getIdCard(){return idCard;} public void setIdCard(String idCard){this.idCard=idCard;}
    public String getPhone(){return phone;} public void setPhone(String phone){this.phone=phone;}
    public String getEmail(){return email;} public void setEmail(String email){this.email=email;}
    public String getBankAccount(){return bankAccount;} public void setBankAccount(String bankAccount){this.bankAccount=bankAccount;}
    public String getCustomerTag(){return customerTag;} public void setCustomerTag(String customerTag){this.customerTag=customerTag;}
    public CustomerGroup getCustomerGroup(){return customerGroup;} public void setCustomerGroup(CustomerGroup customerGroup){this.customerGroup=customerGroup;}
}
