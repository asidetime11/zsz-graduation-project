package com.example.hard06.entity;

import jakarta.persistence.*;

@Entity
public class ConsentRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String purpose;
    private Integer retentionDays;
    private Boolean agreed;

    @ManyToOne
    private Member member;
}
