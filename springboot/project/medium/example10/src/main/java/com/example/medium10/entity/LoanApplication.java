package com.example.medium10.entity;
import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;
@Entity
public class LoanApplication {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(length = 2048)
    private String creditReport;
    private String bankCard;
    private String idCard;
    private String phone;
    private String relativeName;
    private String status;
    @OneToMany(mappedBy = "loanApplication", cascade = CascadeType.ALL)
    private List<LoanReviewNote> notes = new ArrayList<>();
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getCreditReport(){return creditReport;} public void setCreditReport(String creditReport){this.creditReport=creditReport;}
    public String getBankCard(){return bankCard;} public void setBankCard(String bankCard){this.bankCard=bankCard;}
    public String getIdCard(){return idCard;} public void setIdCard(String idCard){this.idCard=idCard;}
    public String getPhone(){return phone;} public void setPhone(String phone){this.phone=phone;}
    public String getRelativeName(){return relativeName;} public void setRelativeName(String relativeName){this.relativeName=relativeName;}
    public String getStatus(){return status;} public void setStatus(String status){this.status=status;}
    public List<LoanReviewNote> getNotes(){return notes;} public void setNotes(List<LoanReviewNote> notes){this.notes=notes;}
}
