package com.example.hard07.entity;

import jakarta.persistence.*;

@Entity
public class IntelRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    @Column(length = 2000)
    private String content;
    private String industry;
    @ManyToOne
    private Supplier supplier;
}
