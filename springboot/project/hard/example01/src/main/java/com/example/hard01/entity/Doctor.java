package com.example.hard01.entity;

import jakarta.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
public class Doctor {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String department;

    @ManyToOne
    private RegionHospital hospital;

    @ManyToMany(mappedBy = "doctors")
    private Set<Patient> patients = new HashSet<>();

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getDepartment() { return department; }
    public void setDepartment(String department) { this.department = department; }
    public RegionHospital getHospital() { return hospital; }
    public void setHospital(RegionHospital hospital) { this.hospital = hospital; }
    public Set<Patient> getPatients() { return patients; }
    public void setPatients(Set<Patient> patients) { this.patients = patients; }
}
