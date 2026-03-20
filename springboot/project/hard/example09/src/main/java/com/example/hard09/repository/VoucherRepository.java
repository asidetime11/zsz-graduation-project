package com.example.hard09.repository;

import com.example.hard09.entity.Voucher;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface VoucherRepository extends JpaRepository<Voucher, Long> {
    List<Voucher> findByCompanyCode(String companyCode);
}
