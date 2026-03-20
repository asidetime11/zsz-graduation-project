package com.example.medium04.repository;
import com.example.medium04.entity.Department;
import org.springframework.data.jpa.repository.JpaRepository;
public interface DepartmentRepository extends JpaRepository<Department,Long>{}
