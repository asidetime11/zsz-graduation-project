package com.example.hard07.controller;

import com.example.hard07.entity.IntelRecord;
import com.example.hard07.service.IntelService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class IntelController {
    private final IntelService intelService;

    public IntelController(IntelService intelService) {
        this.intelService = intelService;
    }

    @GetMapping("/intel/search")
    @ResponseBody
    public List<IntelRecord> search(@RequestParam(defaultValue = "") String keyword,
                                    @RequestParam(defaultValue = "id desc") String sortBy,
                                    @RequestParam(defaultValue = "0") int page,
                                    @RequestParam(defaultValue = "10") int size) {
        return intelService.search(keyword, sortBy, page, size);
    }

    @GetMapping("/intel/report")
    @ResponseBody
    public List<IntelRecord> report(@RequestHeader(value = "X-Org", defaultValue = "branch") String ownerOrg) {
        return intelService.report(ownerOrg);
    }

    @GetMapping("/intel/detail/{id}")
    @ResponseBody
    public IntelRecord detail(@PathVariable Long id) { return intelService.detail(id); }

    @GetMapping("/intel/result")
    public String resultPage(@RequestParam(defaultValue = "") String keyword, Model model) {
        model.addAttribute("rows", intelService.search(keyword, "id desc", 0, 50));
        return "intel_result";
    }

    @GetMapping("/intel/form")
    public String formPage() { return "intel_search"; }

    @GetMapping("/intel/detail-page/{id}")
    public String detailPage(@PathVariable Long id, Model model) {
        model.addAttribute("row", intelService.detail(id));
        return "intel_detail";
    }
}
