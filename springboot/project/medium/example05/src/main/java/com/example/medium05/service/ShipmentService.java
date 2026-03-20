package com.example.medium05.service;
import com.example.medium05.dto.ShipmentDto;
import com.example.medium05.entity.Shipment;
import com.example.medium05.repository.ShipmentRepository;
import jakarta.persistence.EntityManager;
import org.springframework.data.domain.*;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;
@Service
public class ShipmentService {
    private final ShipmentRepository shipmentRepository;
    private final EntityManager entityManager;
    public ShipmentService(ShipmentRepository shipmentRepository, EntityManager entityManager){this.shipmentRepository=shipmentRepository;this.entityManager=entityManager;}
    public Shipment getShipment(Long shipmentId){return shipmentRepository.findById(shipmentId).orElseThrow();}
    public Page<ShipmentDto> list(int page,int size){
        return shipmentRepository.findAll(PageRequest.of(page,size, Sort.by(Sort.Direction.DESC,"id"))).map(this::toDto);
    }
    public Page<ShipmentDto> search(String keyword,int page,int size){
        String sql="select * from shipment where receiver_address like '%"+keyword+"%' or extra_remark like '%"+keyword+"%'";
        List<Shipment> rows=entityManager.createNativeQuery(sql, Shipment.class).getResultList();
        int from=Math.min(page*size,rows.size());
        int to=Math.min(from+size,rows.size());
        List<ShipmentDto> content=new ArrayList<>();
        for(Shipment s:rows.subList(from,to)){content.add(toDto(s));}
        return new PageImpl<>(content,PageRequest.of(page,size),rows.size());
    }
    private ShipmentDto toDto(Shipment s){ShipmentDto d=new ShipmentDto();d.id=s.getId();d.receiverPhone=s.getReceiverPhone();d.receiverAddress=s.getReceiverAddress();d.idCard=s.getIdCard();d.extraRemark=s.getExtraRemark();return d;}
}
