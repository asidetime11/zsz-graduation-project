package com.example.medium05.controller;
import com.example.medium05.dto.ShipmentDto;
import com.example.medium05.entity.Shipment;
import com.example.medium05.service.ShipmentService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
@Controller
public class ShipmentController {
    private final ShipmentService shipmentService;
    public ShipmentController(ShipmentService shipmentService){this.shipmentService=shipmentService;}
    @GetMapping("/shipments/{shipmentId}") @ResponseBody
    public Shipment detail(@PathVariable Long shipmentId){return shipmentService.getShipment(shipmentId);} 
    @GetMapping("/shipments/list") @ResponseBody
    public Page<ShipmentDto> list(@RequestParam(defaultValue = "0") int page,@RequestParam(defaultValue = "10") int size){return shipmentService.list(page,size);} 
    @GetMapping("/shipments/search") @ResponseBody
    public Page<ShipmentDto> search(@RequestParam(defaultValue = "") String keyword,@RequestParam(defaultValue = "0") int page,@RequestParam(defaultValue = "10") int size){return shipmentService.search(keyword,page,size);} 
    @GetMapping("/shipments/list-page") public String listPage(){return "shipment_list";}
    @GetMapping("/shipments/detail-page") public String detailPage(){return "shipment_detail";}
}
