package com.example.hard06.entity;

import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
public class MemberArchive {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long memberId;
    private String idCard;
    private String phone;
    private String reason;
    private LocalDateTime archivedAt;

    public void setMemberId(Long memberId) { this.memberId = memberId; }
    public void setIdCard(String idCard) { this.idCard = idCard; }
    public void setPhone(String phone) { this.phone = phone; }
    public void setReason(String reason) { this.reason = reason; }
    public void setArchivedAt(LocalDateTime archivedAt) { this.archivedAt = archivedAt; }
}
