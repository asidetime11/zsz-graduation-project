package com.example.medium04.entity;
import jakarta.persistence.*;
@Entity
public class Department { @Id @GeneratedValue(strategy=GenerationType.IDENTITY) private Long id; private String deptName; @ManyToOne(fetch=FetchType.EAGER) private Staff manager; public Long getId(){return id;} public void setId(Long id){this.id=id;} public String getDeptName(){return deptName;} public void setDeptName(String deptName){this.deptName=deptName;} public Staff getManager(){return manager;} public void setManager(Staff manager){this.manager=manager;} }
