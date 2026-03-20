package com.example.hard06.controller;

import com.example.hard06.entity.Member;
import com.example.hard06.entity.MemberArchive;
import com.example.hard06.service.MemberService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class MemberController {
    private final MemberService memberService;

    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @PostMapping("/members/register")
    @ResponseBody
    public Member register(Member member) { return memberService.register(member); }

    @PostMapping("/members/deactivate")
    @ResponseBody
    public Member deactivate(@RequestParam Long memberId, @RequestParam(defaultValue = "expired") String reason) {
        return memberService.deactivate(memberId, reason);
    }

    @GetMapping("/members/archive")
    @ResponseBody
    public List<MemberArchive> archive() { return memberService.archive(); }

    @GetMapping("/members/report")
    @ResponseBody
    public List<Member> report(@RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "20") int size) {
        return memberService.report(page, size);
    }

    @GetMapping("/members/list")
    public String listPage(Model model) {
        model.addAttribute("members", memberService.list());
        return "member_list";
    }

    @GetMapping("/members/form")
    public String formPage() {
        return "member_form";
    }

    @GetMapping("/members/archive-page")
    public String archivePage(Model model) {
        model.addAttribute("archives", memberService.archive());
        return "member_archive";
    }
}
