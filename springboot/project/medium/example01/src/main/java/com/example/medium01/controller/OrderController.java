package com.example.medium01.controller;

import com.example.medium01.dto.OrderDetailDto;
import com.example.medium01.entity.AppUser;
import com.example.medium01.entity.OrderRecord;
import com.example.medium01.service.OrderService;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class OrderController {
    private final OrderService orderService;

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @PostMapping("/orders/create")
    @ResponseBody
    public OrderRecord create(@RequestParam String username,
                              @RequestParam String email,
                              @RequestParam String itemName,
                              @RequestParam String idCard,
                              @RequestParam String phone,
                              @RequestParam String paymentCard,
                              @RequestParam String address,
                              @RequestParam(required = false) String secondaryContact) {
        return orderService.createOrder(username, email, itemName, idCard, phone, paymentCard, address, secondaryContact);
    }

    @GetMapping("/orders/{orderId}")
    @ResponseBody
    public OrderDetailDto detail(@PathVariable Long orderId) {
        return orderService.getOrderDetail(orderId);
    }

    @GetMapping("/users")
    @ResponseBody
    public Page<AppUser> users(@RequestParam(defaultValue = "0") int page,
                               @RequestParam(defaultValue = "10") int size) {
        return orderService.listUsers(page, size);
    }

    @GetMapping("/orders/create-page")
    public String createPage() {
        return "create_order";
    }

    @GetMapping("/orders/list-page")
    public String listPage() {
        return "order_list";
    }

    @GetMapping("/orders/detail-page/{orderId}")
    public String detailPage(@PathVariable Long orderId, Model model) {
        model.addAttribute("order", orderService.getOrderDetail(orderId));
        return "order_detail";
    }
}
