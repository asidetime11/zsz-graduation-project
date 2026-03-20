package com.example.easy08.controller;

import com.example.easy08.entity.Feedback;
import com.example.easy08.repository.FeedbackRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class FeedbackController {
    private static final Logger log = LoggerFactory.getLogger(FeedbackController.class);
    private final FeedbackRepository repository;

    public FeedbackController(FeedbackRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/feedback/submit")
    public String form() { return "feedback_form"; }

    @PostMapping("/feedback/submit")
    public String submit(@RequestParam String nickname,
                         @RequestParam String content,
                         @RequestParam String email,
                         @RequestParam String phone,
                         @RequestParam String company) {
        log.info("feedback email={}, phone={}", email, phone);
        Feedback f = new Feedback();
        f.setNickname(nickname);
        f.setContent(content);
        f.setEmail(email);
        f.setPhone(phone);
        f.setCompany(company);
        repository.save(f);
        return "redirect:/feedback/list";
    }

    @GetMapping("/feedback/list")
    public String list(Model model) {
        model.addAttribute("list", repository.findAll());
        return "feedback_list";
    }
}
