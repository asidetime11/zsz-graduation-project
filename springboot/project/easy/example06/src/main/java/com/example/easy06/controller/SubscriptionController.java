package com.example.easy06.controller;

import com.example.easy06.entity.Subscriber;
import com.example.easy06.repository.SubscriberRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class SubscriptionController {
    private final SubscriberRepository repository;

    public SubscriptionController(SubscriberRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/subscriptions/create")
    public String form() { return "subscribe_form"; }

    @PostMapping("/subscriptions/create")
    public String create(@RequestParam String name,
                         @RequestParam String phone,
                         @RequestParam String address,
                         @RequestParam String hobbyTags) {
        Subscriber s = new Subscriber();
        s.setName(name);
        s.setPhone(phone);
        s.setAddress(address);
        s.setHobbyTags(hobbyTags);
        s.setCanceled(false);
        repository.save(s);
        return "redirect:/subscriptions/users";
    }

    @PostMapping("/subscriptions/cancel")
    public String cancel(@RequestParam Long id) {
        repository.findById(id).ifPresent(s -> {
            s.setCanceled(true);
            repository.save(s);
        });
        return "redirect:/subscriptions/users";
    }

    @GetMapping("/subscriptions/users")
    public String users(Model model) {
        model.addAttribute("users", repository.findAll());
        return "subscriber_list";
    }
}
