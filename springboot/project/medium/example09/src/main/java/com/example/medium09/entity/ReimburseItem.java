package com.example.medium09.entity;
import jakarta.persistence.*;
@Entity
public class ReimburseItem {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String itemName;
    private Double amount;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "request_id")
    private ReimburseRequest request;
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getItemName(){return itemName;} public void setItemName(String itemName){this.itemName=itemName;}
    public Double getAmount(){return amount;} public void setAmount(Double amount){this.amount=amount;}
    public ReimburseRequest getRequest(){return request;} public void setRequest(ReimburseRequest request){this.request=request;}
}
