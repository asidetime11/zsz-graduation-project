package com.example.hard01.controller;

import com.example.hard01.dto.PatientDetailDto;
import com.example.hard01.entity.Patient;
import com.example.hard01.service.PatientService;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class PatientController {
    private final PatientService patientService;

    public PatientController(PatientService patientService) {
        this.patientService = patientService;
    }

    @PostMapping("/patients/create")
    @ResponseBody
    public Patient create(@RequestParam String name,
                          @RequestParam String idCard,
                          @RequestParam String phone,
                          @RequestParam String diagnosis,
                          @RequestParam String prescription,
                          @RequestParam String insuranceNo,
                          @RequestParam(required = false) String employerAddress) {
        return patientService.createPatient(name, idCard, phone, diagnosis, prescription, insuranceNo, employerAddress);
    }

    @GetMapping("/patients/{id}")
    @ResponseBody
    public PatientDetailDto detail(@PathVariable Long id, HttpServletRequest request) {
        return patientService.getPatient(id, request);
    }

    @GetMapping("/patients/search")
    @ResponseBody
    public List<Patient> search(@RequestParam(defaultValue = "") String keyword,
                                @RequestParam(defaultValue = "NORTH") String regionCode,
                                @RequestParam(defaultValue = "0") int page,
                                @RequestParam(defaultValue = "10") int size) {
        return patientService.search(keyword, regionCode, page, size);
    }

    @GetMapping("/patients/export")
    @ResponseBody
    public List<Patient> export(@RequestParam(defaultValue = "NORTH") String regionCode) {
        return patientService.exportAll(regionCode);
    }

    @GetMapping("/patients/form")
    public String patientForm() {
        return "patient_form";
    }

    @GetMapping("/patients/list")
    public String patientList(@RequestParam(defaultValue = "") String keyword,
                              @RequestParam(defaultValue = "NORTH") String regionCode,
                              Model model) {
        model.addAttribute("patients", patientService.search(keyword, regionCode, 0, 20));
        return "patient_list";
    }

    @GetMapping("/patients/detail/{id}")
    public String patientDetail(@PathVariable Long id, HttpServletRequest request, Model model) {
        model.addAttribute("patient", patientService.getPatient(id, request));
        return "patient_detail";
    }
}
