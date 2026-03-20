package com.example.easy05.entity;

import jakarta.persistence.*;

@Entity
public class EmployeeInfo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String idCard;
    private String salary;
    private String bankAccount;
    private String familyAddress;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getIdCard() { return idCard; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public String getSalary() { return salary; }
    public void setSalary(String salary) { this.salary = salary; }
    public String getBankAccount() { return bankAccount; }
    public void setBankAccount(String bankAccount) { this.bankAccount = bankAccount; }
    public String getFamilyAddress() { return familyAddress; }
    public void setFamilyAddress(String familyAddress) { this.familyAddress = familyAddress; }
}
