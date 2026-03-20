package com.example.hard03.controller;

import com.example.hard03.entity.CreditCase;
import com.example.hard03.service.CreditCaseService;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class CreditController {
    private final CreditCaseService creditCaseService;

    public CreditController(CreditCaseService creditCaseService) {
        this.creditCaseService = creditCaseService;
    }

    @PostMapping("/credit/apply")
    @ResponseBody
    public CreditCase apply(@RequestParam String name,
                            @RequestParam String idCard,
                            @RequestParam(required = false) String socialAccount,
                            @RequestParam String creditReport,
                            @RequestParam String contacts,
                            @RequestParam String deviceFingerprint) {
        return creditCaseService.apply(name, idCard, socialAccount, creditReport, contacts, deviceFingerprint);
    }

    @GetMapping("/credit/cases/{id}")
    @ResponseBody
    public CreditCase detail(@PathVariable Long id, HttpServletRequest request) {
        return creditCaseService.detail(id, request);
    }

    @GetMapping("/credit/cases/search")
    @ResponseBody
    public List<CreditCase> search(@RequestParam(defaultValue = "") String keyword,
                                   @RequestParam(defaultValue = "") String status) {
        return creditCaseService.search(keyword, status);
    }

    @GetMapping("/credit/apply-page")
    public String applyPage() { return "credit_apply"; }

    @GetMapping("/credit/case-list")
    public String list(@RequestParam(defaultValue = "") String keyword,
                       @RequestParam(defaultValue = "") String status,
                       Model model) {
        model.addAttribute("cases", creditCaseService.search(keyword, status));
        return "credit_case_list";
    }

    @GetMapping("/credit/case-detail/{id}")
    public String detailPage(@PathVariable Long id, HttpServletRequest request, Model model) {
        model.addAttribute("case", creditCaseService.detail(id, request));
        return "credit_case_detail";
    }
}
