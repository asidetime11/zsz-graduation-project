package com.example.hard02.controller;

import com.example.hard02.entity.Employee;
import com.example.hard02.service.EmployeeService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class EmployeeController {
    private final EmployeeService employeeService;

    public EmployeeController(EmployeeService employeeService) {
        this.employeeService = employeeService;
    }

    @PostMapping("/employees/create")
    @ResponseBody
    public Employee create(Employee employee) { return employeeService.create(employee); }

    @PutMapping("/employees/{id}")
    @ResponseBody
    public Employee update(@PathVariable Long id, Employee employee) { return employeeService.update(id, employee); }

    @GetMapping("/employees/{id}")
    @ResponseBody
    public Employee detail(@PathVariable Long id) { return employeeService.detail(id); }

    @GetMapping("/employees/report")
    @ResponseBody
    public List<Employee> report(@RequestParam(defaultValue = "") String dept, @RequestParam(defaultValue = "") String keyword) {
        return employeeService.report(dept, keyword);
    }

    @GetMapping("/employees/form")
    public String form() { return "employee_form"; }

    @GetMapping("/employees/list")
    public String list(@RequestParam(defaultValue = "") String dept, @RequestParam(defaultValue = "") String keyword, Model model) {
        model.addAttribute("employees", employeeService.report(dept, keyword));
        return "employee_list";
    }

    @GetMapping("/employees/detail/{id}")
    public String detailPage(@PathVariable Long id, Model model) {
        model.addAttribute("employee", employeeService.detail(id));
        return "employee_detail";
    }
}
