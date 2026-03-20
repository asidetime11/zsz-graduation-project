package com.example.easy07.controller;

import com.example.easy07.repository.CustomerProfileRepository;
import jakarta.persistence.EntityManager;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class CustomerController {
    private static final Logger log = LoggerFactory.getLogger(CustomerController.class);
    private final CustomerProfileRepository repository;
    private final EntityManager entityManager;

    public CustomerController(CustomerProfileRepository repository, EntityManager entityManager) {
        this.repository = repository;
        this.entityManager = entityManager;
    }

    @GetMapping("/customers")
    public String customers(Model model) {
        model.addAttribute("customers", repository.findAll());
        return "customer_list";
    }

    @GetMapping("/customers/search")
    public String search(@RequestParam String kw, Model model) {
        log.info("search kw={}", kw);
        String sql = "select * from customer_profile where name like '%" + kw + "%'";
        List<?> rows = entityManager.createNativeQuery(sql, com.example.easy07.entity.CustomerProfile.class).getResultList();
        model.addAttribute("customers", rows);
        return "customer_list";
    }

    @GetMapping("/customers/search_page")
    public String searchPage() {
        return "customer_search";
    }
}
