package com.example.medium07.entity;
import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;
@Entity
public class CustomerGroup {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String groupName;
    @OneToMany(mappedBy = "customerGroup")
    private List<Customer> customers = new ArrayList<>();
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getGroupName(){return groupName;} public void setGroupName(String groupName){this.groupName=groupName;}
    public List<Customer> getCustomers(){return customers;} public void setCustomers(List<Customer> customers){this.customers=customers;}
}
