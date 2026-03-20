package com.example.medium05.repository;
import com.example.medium05.entity.Shipment;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
public interface ShipmentRepository extends JpaRepository<Shipment, Long> {
    Page<Shipment> findByReceiverAddressContaining(String receiverAddress, Pageable pageable);
}
