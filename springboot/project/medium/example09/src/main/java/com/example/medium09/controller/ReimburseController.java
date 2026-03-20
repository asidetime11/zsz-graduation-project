package com.example.medium09.controller;
import com.example.medium09.dto.ReimburseDto;
import com.example.medium09.entity.ReimburseRequest;
import com.example.medium09.service.ReimburseService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
@Controller
public class ReimburseController {
    private final ReimburseService reimburseService;
    public ReimburseController(ReimburseService reimburseService){this.reimburseService=reimburseService;}
    @PostMapping("/reimburse/apply") @ResponseBody
    public ReimburseRequest apply(@RequestBody ReimburseRequest request){return reimburseService.apply(request);} 
    @GetMapping("/reimburse/{id}") @ResponseBody
    public ReimburseRequest detail(@PathVariable Long id){return reimburseService.detail(id);} 
    @GetMapping("/reimburse/list") @ResponseBody
    public Page<ReimburseDto> list(@RequestParam(defaultValue = "") String status,@RequestParam(defaultValue = "0") int page,@RequestParam(defaultValue = "10") int size){return reimburseService.list(status,page,size);} 
    @GetMapping("/reimburse/form-page") public String formPage(){return "reimburse_form";}
    @GetMapping("/reimburse/detail-page") public String detailPage(){return "reimburse_detail";}
}
