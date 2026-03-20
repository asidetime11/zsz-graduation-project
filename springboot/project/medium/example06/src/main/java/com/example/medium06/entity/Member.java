package com.example.medium06.entity;
import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
@Entity
public class Member {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String phone;
    private String idCard;
    private String address;
    private String interestTags;
    private String status;
    private LocalDateTime createdAt = LocalDateTime.now();
    @OneToMany(mappedBy = "member", cascade = CascadeType.ALL)
    private List<MemberHistory> histories = new ArrayList<>();
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getPhone(){return phone;} public void setPhone(String phone){this.phone=phone;}
    public String getIdCard(){return idCard;} public void setIdCard(String idCard){this.idCard=idCard;}
    public String getAddress(){return address;} public void setAddress(String address){this.address=address;}
    public String getInterestTags(){return interestTags;} public void setInterestTags(String interestTags){this.interestTags=interestTags;}
    public String getStatus(){return status;} public void setStatus(String status){this.status=status;}
    public LocalDateTime getCreatedAt(){return createdAt;} public void setCreatedAt(LocalDateTime createdAt){this.createdAt=createdAt;}
    public List<MemberHistory> getHistories(){return histories;} public void setHistories(List<MemberHistory> histories){this.histories=histories;}
}
