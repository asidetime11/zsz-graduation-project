package com.example.hard04.entity;

import jakarta.persistence.*;

@Entity
public class DepartmentShare {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String sourceDept;
    private String targetDept;
    @ManyToOne
    private GovCase govCase;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getSourceDept() { return sourceDept; }
    public void setSourceDept(String sourceDept) { this.sourceDept = sourceDept; }
    public String getTargetDept() { return targetDept; }
    public void setTargetDept(String targetDept) { this.targetDept = targetDept; }
    public GovCase getGovCase() { return govCase; }
    public void setGovCase(GovCase govCase) { this.govCase = govCase; }
}
