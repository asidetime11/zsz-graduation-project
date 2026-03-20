package com.example.medium06.entity;
import jakarta.persistence.*;
import java.time.LocalDateTime;
@Entity
public class MemberHistory {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String actionType;
    private LocalDateTime actionTime = LocalDateTime.now();
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "member_id")
    private Member member;
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getActionType(){return actionType;} public void setActionType(String actionType){this.actionType=actionType;}
    public LocalDateTime getActionTime(){return actionTime;} public void setActionTime(LocalDateTime actionTime){this.actionTime=actionTime;}
    public Member getMember(){return member;} public void setMember(Member member){this.member=member;}
}
