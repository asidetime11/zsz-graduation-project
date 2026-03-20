package com.example.hard09.entity;

import jakarta.persistence.*;

import java.time.LocalDate;

@Entity
public class LedgerSet {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String setName;
    private LocalDate closedDate;
    private String status;
}
