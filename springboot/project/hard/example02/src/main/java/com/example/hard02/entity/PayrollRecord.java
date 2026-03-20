package com.example.hard02.entity;

import jakarta.persistence.*;

@Entity
public class PayrollRecord {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String payMonth;
    private String amount;
    @ManyToOne
    private Employee employee;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getPayMonth() { return payMonth; }
    public void setPayMonth(String payMonth) { this.payMonth = payMonth; }
    public String getAmount() { return amount; }
    public void setAmount(String amount) { this.amount = amount; }
    public Employee getEmployee() { return employee; }
    public void setEmployee(Employee employee) { this.employee = employee; }
}
