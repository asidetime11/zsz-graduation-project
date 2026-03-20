package com.example.medium08.entity;
import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;
@Entity
public class Ticket {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String email;
    private String phone;
    @OneToMany(mappedBy = "ticket", cascade = CascadeType.ALL)
    private List<TicketComment> comments = new ArrayList<>();
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getTitle(){return title;} public void setTitle(String title){this.title=title;}
    public String getEmail(){return email;} public void setEmail(String email){this.email=email;}
    public String getPhone(){return phone;} public void setPhone(String phone){this.phone=phone;}
    public List<TicketComment> getComments(){return comments;} public void setComments(List<TicketComment> comments){this.comments=comments;}
}
