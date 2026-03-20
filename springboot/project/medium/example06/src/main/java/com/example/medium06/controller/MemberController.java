package com.example.medium06.controller;
import com.example.medium06.dto.MemberHistoryDto;
import com.example.medium06.entity.Member;
import com.example.medium06.service.MemberService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
@Controller
public class MemberController {
    private final MemberService memberService;
    public MemberController(MemberService memberService){this.memberService=memberService;}
    @PostMapping("/members/register") @ResponseBody
    public Member register(@RequestBody Member member){return memberService.register(member);} 
    @PostMapping("/members/cancel") @ResponseBody
    public Member cancel(@RequestParam Long memberId){return memberService.cancel(memberId);} 
    @GetMapping("/members/history") @ResponseBody
    public Page<MemberHistoryDto> history(@RequestParam(defaultValue = "") String keyword,@RequestParam(defaultValue = "0") int page,@RequestParam(defaultValue = "10") int size){return memberService.history(keyword,page,size);} 
    @GetMapping("/members/register-page") public String registerPage(){return "member_register";}
    @GetMapping("/members/history-page") public String historyPage(){return "member_history";}
}
