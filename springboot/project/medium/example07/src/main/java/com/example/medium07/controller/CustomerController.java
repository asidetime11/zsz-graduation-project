package com.example.medium07.controller;
import com.example.medium07.dto.CustomerDto;
import com.example.medium07.service.CustomerService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
@Controller
public class CustomerController {
    private final CustomerService customerService;
    public CustomerController(CustomerService customerService){this.customerService=customerService;}
    @GetMapping("/customers/search") @ResponseBody
    public Page<CustomerDto> search(@RequestParam(defaultValue = "") String keyword,@RequestParam(defaultValue = "0") int page,@RequestParam(defaultValue = "10") int size){return customerService.search(keyword,page,size);} 
    @GetMapping("/customers/filter") @ResponseBody
    public Page<CustomerDto> filter(@RequestParam(defaultValue = "") String customerTag,@RequestParam(defaultValue = "0") int page,@RequestParam(defaultValue = "10") int size){return customerService.filter(customerTag,page,size);} 
    @GetMapping("/customers/search-page") public String searchPage(){return "customer_search";}
    @GetMapping("/customers/result-page") public String resultPage(){return "customer_result";}
}
