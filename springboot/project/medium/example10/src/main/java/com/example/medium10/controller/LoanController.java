package com.example.medium10.controller;
import com.example.medium10.dto.LoanReviewDto;
import com.example.medium10.entity.LoanApplication;
import com.example.medium10.service.LoanService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
@Controller
public class LoanController {
    private final LoanService loanService;
    public LoanController(LoanService loanService){this.loanService=loanService;}
    @PostMapping("/loan/apply") @ResponseBody
    public LoanApplication apply(@RequestBody LoanApplication request){return loanService.apply(request);} 
    @GetMapping("/loan/review/{id}") @ResponseBody
    public LoanApplication review(@PathVariable Long id){return loanService.review(id);} 
    @GetMapping("/loan/review/list") @ResponseBody
    public Page<LoanReviewDto> reviewList(@RequestParam(defaultValue = "") String keyword,@RequestParam(defaultValue = "0") int page,@RequestParam(defaultValue = "10") int size){return loanService.reviewList(keyword,page,size);} 
    @GetMapping("/loan/apply-page") public String applyPage(){return "loan_apply";}
    @GetMapping("/loan/review-page") public String reviewPage(){return "loan_review";}
}
