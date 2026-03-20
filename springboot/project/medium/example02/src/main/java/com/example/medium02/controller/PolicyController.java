package com.example.medium02.controller;

import com.example.medium02.dto.ApplicantDto;
import com.example.medium02.entity.PolicyRecord;
import com.example.medium02.service.PolicyService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
public class PolicyController {
    private final PolicyService policyService;

    public PolicyController(PolicyService policyService) {
        this.policyService = policyService;
    }

    @PostMapping("/policies/apply")
    @ResponseBody
    public PolicyRecord apply(@RequestParam String name,
                              @RequestParam String policyType,
                              @RequestParam String idCard,
                              @RequestParam String bankAccount,
                              @RequestParam String medicalHistory,
                              @RequestParam(required = false) String religion,
                              @RequestParam(required = false) String familyGeneticTags) {
        return policyService.apply(name, policyType, idCard, bankAccount, medicalHistory, religion, familyGeneticTags);
    }

    @GetMapping("/policies/applicants")
    @ResponseBody
    public Page<ApplicantDto> applicants(@RequestParam(defaultValue = "0") int page,
                                         @RequestParam(defaultValue = "10") int size) {
        return policyService.list(page, size);
    }

    @GetMapping("/policy/apply-page")
    public String applyPage() {
        return "policy_apply";
    }

    @GetMapping("/policy/list-page")
    public String listPage() {
        return "applicant_list";
    }
}
