package com.example.hard05.controller;

import com.example.hard05.entity.ClaimCase;
import com.example.hard05.service.ClaimService;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class ClaimController {
    private final ClaimService claimService;

    public ClaimController(ClaimService claimService) {
        this.claimService = claimService;
    }

    @PostMapping("/claims/create")
    @ResponseBody
    public ClaimCase create(ClaimCase claimCase) { return claimService.create(claimCase); }

    @PutMapping("/claims/{id}")
    @ResponseBody
    public ClaimCase update(@PathVariable Long id, ClaimCase claimCase) { return claimService.update(id, claimCase); }

    @GetMapping("/claims/{claimId}")
    @ResponseBody
    public ClaimCase detail(@PathVariable Long claimId, HttpServletRequest request) { return claimService.detail(claimId, request); }

    @GetMapping("/claims/search")
    @ResponseBody
    public List<ClaimCase> search(@RequestParam(defaultValue = "") String keyword,
                                  @RequestParam(defaultValue = "INST-A") String institutionCode,
                                  @RequestParam(defaultValue = "") String status,
                                  @RequestParam(defaultValue = "id desc") String sortBy) {
        return claimService.search(keyword, institutionCode, status, sortBy);
    }

    @GetMapping("/claims/export")
    @ResponseBody
    public List<ClaimCase> export(@RequestParam(defaultValue = "INST-A") String institutionCode,
                                  @RequestParam(defaultValue = "") String status,
                                  @RequestParam(defaultValue = "all") String dateRange) {
        return claimService.export(institutionCode, status, dateRange);
    }

    @GetMapping("/claims/list")
    public String list(@RequestParam(defaultValue = "") String keyword,
                       @RequestParam(defaultValue = "INST-A") String institutionCode,
                       @RequestParam(defaultValue = "") String status,
                       Model model) {
        model.addAttribute("claims", claimService.search(keyword, institutionCode, status, "id desc"));
        return "claim_list";
    }

    @GetMapping("/claims/detail-page/{claimId}")
    public String detailPage(@PathVariable Long claimId, HttpServletRequest request, Model model) {
        model.addAttribute("claim", claimService.detail(claimId, request));
        return "claim_detail";
    }

    @GetMapping("/claims/export-page")
    public String exportPage(@RequestParam(defaultValue = "INST-A") String institutionCode,
                             @RequestParam(defaultValue = "") String status,
                             Model model) {
        model.addAttribute("claims", claimService.export(institutionCode, status, "all"));
        return "claim_export";
    }
}
