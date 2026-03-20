package com.example.hard05.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
public class ClaimExportLog {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String operator;
    private String filters;
    private LocalDateTime createdAt;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getOperator() { return operator; }
    public void setOperator(String operator) { this.operator = operator; }
    public String getFilters() { return filters; }
    public void setFilters(String filters) { this.filters = filters; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
