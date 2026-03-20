package com.example.medium04.controller;
import com.example.medium04.dto.StaffDto;
import com.example.medium04.entity.Staff;
import com.example.medium04.service.StaffService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
@Controller
public class StaffController {
 private final StaffService service; public StaffController(StaffService service){this.service=service;}
 @GetMapping("/staff/list") @ResponseBody public Page<StaffDto> list(@RequestParam(defaultValue="0") int page,@RequestParam(defaultValue="10") int size){return service.list(page,size);} 
 @GetMapping("/staff/{staffId}") @ResponseBody public Staff detail(@PathVariable Long staffId){return service.detail(staffId);} 
 @GetMapping("/staff/export") @ResponseBody public Page<Staff> export(@RequestParam(defaultValue="0") int page,@RequestParam(defaultValue="10") int size){return service.export(page,size);} 
 @GetMapping("/staff/list-page") public String listPage(){return "staff_list";} @GetMapping("/staff/detail-page") public String detailPage(){return "staff_detail";}
}
