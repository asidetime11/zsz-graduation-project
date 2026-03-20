package com.example.medium05.entity;
import jakarta.persistence.*;
import java.time.LocalDateTime;
@Entity
public class Shipment {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String receiverPhone;
    private String receiverAddress;
    private String idCard;
    private String extraRemark;
    private Long ownerId;
    private LocalDateTime createdAt = LocalDateTime.now();
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "courier_id")
    private Courier courier;
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getReceiverPhone(){return receiverPhone;} public void setReceiverPhone(String receiverPhone){this.receiverPhone=receiverPhone;}
    public String getReceiverAddress(){return receiverAddress;} public void setReceiverAddress(String receiverAddress){this.receiverAddress=receiverAddress;}
    public String getIdCard(){return idCard;} public void setIdCard(String idCard){this.idCard=idCard;}
    public String getExtraRemark(){return extraRemark;} public void setExtraRemark(String extraRemark){this.extraRemark=extraRemark;}
    public Long getOwnerId(){return ownerId;} public void setOwnerId(Long ownerId){this.ownerId=ownerId;}
    public LocalDateTime getCreatedAt(){return createdAt;} public void setCreatedAt(LocalDateTime createdAt){this.createdAt=createdAt;}
    public Courier getCourier(){return courier;} public void setCourier(Courier courier){this.courier=courier;}
}
