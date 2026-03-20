package com.example.easy01.controller;

import com.example.easy01.entity.UserProfile;
import com.example.easy01.repository.UserProfileRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class UserController {
    private final UserProfileRepository userProfileRepository;

    public UserController(UserProfileRepository userProfileRepository) {
        this.userProfileRepository = userProfileRepository;
    }

    @GetMapping("/register")
    public String registerForm() {
        return "register";
    }

    @PostMapping("/register")
    public String register(
            @RequestParam String name,
            @RequestParam String idCard,
            @RequestParam String phone,
            @RequestParam String bankAccount,
            @RequestParam Integer familyMembers) {
        UserProfile user = new UserProfile();
        user.setName(name);
        user.setIdCard(idCard);
        user.setPhone(phone);
        user.setBankAccount(bankAccount);
        user.setFamilyMembers(familyMembers);
        userProfileRepository.save(user);
        return "redirect:/users";
    }

    @GetMapping("/users")
    public String users(Model model) {
        model.addAttribute("users", userProfileRepository.findAll());
        return "user_list";
    }
}
