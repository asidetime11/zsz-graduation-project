package com.example.hard10.controller;

import com.example.hard10.entity.LoanApplication;
import com.example.hard10.service.LoanApplicationService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class LoanApplicationController {
    private final LoanApplicationService loanApplicationService;

    public LoanApplicationController(LoanApplicationService loanApplicationService) {
        this.loanApplicationService = loanApplicationService;
    }

    @PostMapping("/applications/create")
    @ResponseBody
    public LoanApplication create(LoanApplication app) { return loanApplicationService.create(app); }

    @GetMapping("/applications/{id}")
    @ResponseBody
    public LoanApplication detail(@PathVariable Long id, @RequestHeader(value = "X-Org", defaultValue = "ORG-A") String orgCode) {
        return loanApplicationService.getById(id, orgCode);
    }

    @GetMapping("/applications/search")
    @ResponseBody
    public List<LoanApplication> search(@RequestParam(defaultValue = "") String keyword,
                                        @RequestParam(defaultValue = "id desc") String orderBy,
                                        @RequestParam(defaultValue = "") String status) {
        return loanApplicationService.search(keyword, orderBy, status);
    }

    @GetMapping("/applications/export")
    @ResponseBody
    public List<LoanApplication> export(@RequestHeader(value = "X-Org", defaultValue = "ORG-A") String orgCode) {
        return loanApplicationService.export(orgCode);
    }

    @GetMapping("/applications/form")
    public String formPage() { return "application_form"; }

    @GetMapping("/applications/list")
    public String listPage(@RequestParam(defaultValue = "") String keyword, Model model) {
        model.addAttribute("apps", loanApplicationService.search(keyword, "id desc", ""));
        return "application_list";
    }

    @GetMapping("/applications/detail-page/{id}")
    public String detailPage(@PathVariable Long id, @RequestHeader(value = "X-Org", defaultValue = "ORG-A") String orgCode, Model model) {
        model.addAttribute("app", loanApplicationService.getById(id, orgCode));
        return "application_detail";
    }
}
