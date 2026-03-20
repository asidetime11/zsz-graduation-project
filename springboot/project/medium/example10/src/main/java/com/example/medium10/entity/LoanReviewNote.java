package com.example.medium10.entity;
import jakarta.persistence.*;
@Entity
public class LoanReviewNote {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String reviewer;
    @Column(length = 2000)
    private String note;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "loan_id")
    private LoanApplication loanApplication;
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getReviewer(){return reviewer;} public void setReviewer(String reviewer){this.reviewer=reviewer;}
    public String getNote(){return note;} public void setNote(String note){this.note=note;}
    public LoanApplication getLoanApplication(){return loanApplication;} public void setLoanApplication(LoanApplication loanApplication){this.loanApplication=loanApplication;}
}
