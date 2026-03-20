package com.example.hard04.controller;

import com.example.hard04.entity.GovCase;
import com.example.hard04.service.CaseService;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class CaseController {
    private final CaseService caseService;

    public CaseController(CaseService caseService) {
        this.caseService = caseService;
    }

    @GetMapping("/cases/{caseId}")
    @ResponseBody
    public GovCase caseDetail(@PathVariable Long caseId, HttpServletRequest request) {
        return caseService.caseDetail(caseId, request);
    }

    @GetMapping("/cases/share")
    @ResponseBody
    public List<GovCase> share(@RequestParam(defaultValue = "all") String targetDept,
                               @RequestParam(defaultValue = "") String status) {
        return caseService.share(targetDept, status);
    }

    @GetMapping("/cases/archive")
    @ResponseBody
    public List<GovCase> archive() {
        return caseService.archive();
    }

    @GetMapping("/cases/list")
    public String list(@RequestParam(defaultValue = "all") String targetDept,
                       @RequestParam(defaultValue = "") String status,
                       Model model) {
        model.addAttribute("cases", caseService.share(targetDept, status));
        return "case_list";
    }

    @GetMapping("/cases/detail-page/{caseId}")
    public String detailPage(@PathVariable Long caseId, HttpServletRequest request, Model model) {
        model.addAttribute("case", caseService.caseDetail(caseId, request));
        return "case_detail";
    }

    @GetMapping("/cases/audit")
    public String audit(Model model) {
        model.addAttribute("archive", caseService.archive());
        return "case_audit";
    }
}
