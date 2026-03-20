package com.example.easy05.controller;

import com.example.easy05.repository.EmployeeInfoRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class EmployeeController {
    private static final Logger log = LoggerFactory.getLogger(EmployeeController.class);
    private final EmployeeInfoRepository repository;

    public EmployeeController(EmployeeInfoRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/employees")
    public String list(Model model) {
        model.addAttribute("employees", repository.findAll());
        return "employee_list";
    }

    @GetMapping("/employees/{id}")
    public String detail(@PathVariable Long id, Model model) {
        var employee = repository.findById(id).orElse(null);
        if (employee != null) {
            log.info("employee detail query idCard={}", employee.getIdCard());
        }
        model.addAttribute("employee", employee);
        return "employee_detail";
    }
}
