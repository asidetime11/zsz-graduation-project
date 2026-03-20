package com.example.medium07.repository;
import com.example.medium07.entity.Customer;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
public interface CustomerRepository extends JpaRepository<Customer, Long> {
    Page<Customer> findByCustomerTagContaining(String customerTag, Pageable pageable);
}
