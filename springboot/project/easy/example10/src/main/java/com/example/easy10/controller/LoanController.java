package com.example.easy10.controller;

import com.example.easy10.repository.LoanApplicationRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class LoanController {
    private final LoanApplicationRepository repository;

    public LoanController(LoanApplicationRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/loan/apply")
    public String form() { return "loan_apply"; }

    @PostMapping("/loan/apply")
    public String apply(@RequestParam String applicantName,
                        @RequestParam String idCard,
                        @RequestParam String bankCard,
                        @RequestParam String incomeProof,
                        @RequestParam String relativeContact) {
        var loan = new com.example.easy10.entity.LoanApplication();
        loan.setApplicantName(applicantName);
        loan.setIdCard(idCard);
        loan.setBankCard(bankCard);
        loan.setIncomeProof(incomeProof);
        loan.setRelativeContact(relativeContact);
        repository.save(loan);
        return "redirect:/loan/" + loan.getId();
    }

    @GetMapping("/loan/{id}")
    public String detail(@PathVariable Long id, Model model) {
        model.addAttribute("loan", repository.findById(id).orElse(null));
        return "loan_detail";
    }
}
