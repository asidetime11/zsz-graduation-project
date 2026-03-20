package com.example.hard01.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
public class VisitRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private LocalDateTime visitTime;
    private String note;

    @ManyToOne
    private Patient patient;

    @ManyToOne
    private Doctor doctor;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public LocalDateTime getVisitTime() { return visitTime; }
    public void setVisitTime(LocalDateTime visitTime) { this.visitTime = visitTime; }
    public String getNote() { return note; }
    public void setNote(String note) { this.note = note; }
    public Patient getPatient() { return patient; }
    public void setPatient(Patient patient) { this.patient = patient; }
    public Doctor getDoctor() { return doctor; }
    public void setDoctor(Doctor doctor) { this.doctor = doctor; }
}
