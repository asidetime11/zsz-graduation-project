package com.example.easy03.controller;

import com.example.easy03.entity.PatientRecord;
import com.example.easy03.repository.PatientRecordRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class AppointmentController {
    private final PatientRecordRepository repository;

    public AppointmentController(PatientRecordRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/appointments/book")
    public String form() {
        return "appointment_form";
    }

    @PostMapping("/appointments/book")
    public String book(@RequestParam String name,
                       @RequestParam String idCard,
                       @RequestParam String medicalHistory,
                       @RequestParam String phone,
                       @RequestParam String occupation) {
        PatientRecord p = new PatientRecord();
        p.setName(name);
        p.setIdCard(idCard);
        p.setMedicalHistory(medicalHistory);
        p.setPhone(phone);
        p.setOccupation(occupation);
        repository.save(p);
        return "redirect:/patients";
    }

    @GetMapping("/patients")
    public String patients(Model model) {
        model.addAttribute("patients", repository.findAll());
        return "patient_list";
    }
}
