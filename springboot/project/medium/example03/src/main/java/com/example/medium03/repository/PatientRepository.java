package com.example.medium03.repository;
import com.example.medium03.entity.Patient;
import org.springframework.data.jpa.repository.JpaRepository;
public interface PatientRepository extends JpaRepository<Patient,Long>{}
