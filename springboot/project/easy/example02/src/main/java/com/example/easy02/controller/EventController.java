package com.example.easy02.controller;

import com.example.easy02.entity.EventApplicant;
import com.example.easy02.repository.EventApplicantRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class EventController {
    private final EventApplicantRepository repository;

    public EventController(EventApplicantRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/events/apply")
    public String applyForm() {
        return "apply_form";
    }

    @PostMapping("/events/apply")
    public String apply(@RequestParam String studentName,
                        @RequestParam String studentPhone,
                        @RequestParam String emergencyPhone,
                        @RequestParam String parentJob,
                        @RequestParam String annualIncome) {
        EventApplicant a = new EventApplicant();
        a.setStudentName(studentName);
        a.setStudentPhone(studentPhone);
        a.setEmergencyPhone(emergencyPhone);
        a.setParentJob(parentJob);
        a.setAnnualIncome(annualIncome);
        repository.save(a);
        return "redirect:/events/applicants";
    }

    @GetMapping("/events/applicants")
    public String applicants(Model model) {
        model.addAttribute("applicants", repository.findAll());
        return "applicant_list";
    }
}
