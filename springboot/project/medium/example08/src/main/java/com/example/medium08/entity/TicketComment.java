package com.example.medium08.entity;
import jakarta.persistence.*;
import java.time.LocalDateTime;
@Entity
public class TicketComment {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(length = 2000)
    private String content;
    private String email;
    private String phone;
    private String homeAddress;
    private LocalDateTime createdAt = LocalDateTime.now();
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "ticket_id")
    private Ticket ticket;
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getContent(){return content;} public void setContent(String content){this.content=content;}
    public String getEmail(){return email;} public void setEmail(String email){this.email=email;}
    public String getPhone(){return phone;} public void setPhone(String phone){this.phone=phone;}
    public String getHomeAddress(){return homeAddress;} public void setHomeAddress(String homeAddress){this.homeAddress=homeAddress;}
    public LocalDateTime getCreatedAt(){return createdAt;} public void setCreatedAt(LocalDateTime createdAt){this.createdAt=createdAt;}
    public Ticket getTicket(){return ticket;} public void setTicket(Ticket ticket){this.ticket=ticket;}
}
