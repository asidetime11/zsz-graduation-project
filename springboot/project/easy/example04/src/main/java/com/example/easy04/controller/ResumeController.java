package com.example.easy04.controller;

import com.example.easy04.entity.ResumeCandidate;
import com.example.easy04.repository.ResumeCandidateRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class ResumeController {
    private final ResumeCandidateRepository repository;

    public ResumeController(ResumeCandidateRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/resume/submit")
    public String form() { return "resume_submit"; }

    @PostMapping("/resume/submit")
    public String submit(@RequestParam String name,
                         @RequestParam String idCard,
                         @RequestParam String phone,
                         @RequestParam String email,
                         @RequestParam String maritalStatus,
                         @RequestParam String fertilityPlan) {
        ResumeCandidate c = new ResumeCandidate();
        c.setName(name);
        c.setIdCard(idCard);
        c.setPhone(phone);
        c.setEmail(email);
        c.setMaritalStatus(maritalStatus);
        c.setFertilityPlan(fertilityPlan);
        repository.save(c);
        return "redirect:/resume/candidates";
    }

    @GetMapping("/resume/candidates")
    public String candidates(Model model) {
        model.addAttribute("candidates", repository.findAll());
        return "candidate_list";
    }
}
