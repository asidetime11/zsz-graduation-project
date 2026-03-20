package com.example.medium05.entity;
import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;
@Entity
public class Courier {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String region;
    @OneToMany(mappedBy = "courier")
    private List<Shipment> shipments = new ArrayList<>();
    public Long getId(){return id;} public void setId(Long id){this.id=id;}
    public String getName(){return name;} public void setName(String name){this.name=name;}
    public String getRegion(){return region;} public void setRegion(String region){this.region=region;}
    public List<Shipment> getShipments(){return shipments;} public void setShipments(List<Shipment> shipments){this.shipments=shipments;}
}
