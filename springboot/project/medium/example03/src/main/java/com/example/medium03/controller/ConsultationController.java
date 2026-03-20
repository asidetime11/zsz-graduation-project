package com.example.medium03.controller;
import com.example.medium03.dto.ConsultationDto;
import com.example.medium03.entity.Consultation;
import com.example.medium03.entity.Patient;
import com.example.medium03.service.ConsultationService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
@Controller
public class ConsultationController {
 private final ConsultationService service;
 public ConsultationController(ConsultationService service){this.service=service;}
 @PostMapping("/consultations/submit") @ResponseBody
 public Consultation submit(@RequestParam String name,@RequestParam String idCard,@RequestParam String phone,@RequestParam(required=false) String workUnit,@RequestParam String diagnosis,@RequestParam String prescription){ return service.submit(name,idCard,phone,workUnit,diagnosis,prescription);} 
 @GetMapping("/consultations/{id}") @ResponseBody public ConsultationDto detail(@PathVariable Long id){ return service.detail(id);} 
 @GetMapping("/patients/list") @ResponseBody public Page<Patient> list(@RequestParam(defaultValue="0") int page,@RequestParam(defaultValue="10") int size){ return service.patients(page,size);} 
 @GetMapping("/consult/form-page") public String form(){ return "consult_form";} @GetMapping("/consult/detail-page") public String detailPage(){ return "consult_detail";}
}
