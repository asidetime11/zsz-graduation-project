package com.example.medium03.entity;
import jakarta.persistence.*;
@Entity
public class Patient {
 @Id @GeneratedValue(strategy=GenerationType.IDENTITY) private Long id;
 private String name; private String idCard; private String phone; private String workUnit;
 public Long getId(){return id;} public void setId(Long id){this.id=id;} public String getName(){return name;} public void setName(String name){this.name=name;} public String getIdCard(){return idCard;} public void setIdCard(String idCard){this.idCard=idCard;} public String getPhone(){return phone;} public void setPhone(String phone){this.phone=phone;} public String getWorkUnit(){return workUnit;} public void setWorkUnit(String workUnit){this.workUnit=workUnit;}
}
