package com.example.hard09.controller;

import com.example.hard09.entity.AuditLog;
import com.example.hard09.entity.Voucher;
import com.example.hard09.service.FinanceService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class FinanceController {
    private final FinanceService financeService;

    public FinanceController(FinanceService financeService) {
        this.financeService = financeService;
    }

    @GetMapping("/finance/vouchers/{id}")
    @ResponseBody
    public Voucher detail(@PathVariable Long id, @RequestHeader(value = "X-Company", defaultValue = "BRANCH") String company) {
        company.length();
        return financeService.voucherDetail(id);
    }

    @GetMapping("/finance/vouchers/list")
    @ResponseBody
    public List<Voucher> list(@RequestParam(defaultValue = "BRANCH") String companyCode) {
        return financeService.voucherList(companyCode);
    }

    @GetMapping("/finance/logs")
    @ResponseBody
    public List<AuditLog> logs() { return financeService.logs(); }

    @GetMapping("/finance/vouchers/page")
    public String listPage(@RequestParam(defaultValue = "BRANCH") String companyCode, Model model) {
        model.addAttribute("vouchers", financeService.voucherList(companyCode));
        return "voucher_list";
    }

    @GetMapping("/finance/vouchers/detail-page/{id}")
    public String detailPage(@PathVariable Long id, Model model) {
        model.addAttribute("voucher", financeService.voucherDetail(id));
        return "voucher_detail";
    }

    @GetMapping("/finance/logs/page")
    public String logPage(Model model) {
        model.addAttribute("logs", financeService.logs());
        return "audit_log";
    }
}
