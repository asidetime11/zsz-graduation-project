package com.example.medium04.repository;
import com.example.medium04.entity.Staff;
import org.springframework.data.jpa.repository.JpaRepository;
public interface StaffRepository extends JpaRepository<Staff,Long>{}
