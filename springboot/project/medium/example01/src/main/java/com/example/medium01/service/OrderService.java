package com.example.medium01.service;

import com.example.medium01.dto.OrderDetailDto;
import com.example.medium01.entity.AppUser;
import com.example.medium01.entity.OrderRecord;
import com.example.medium01.repository.AppUserRepository;
import com.example.medium01.repository.OrderRecordRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

@Service
public class OrderService {
    private final AppUserRepository userRepository;
    private final OrderRecordRepository orderRepository;

    public OrderService(AppUserRepository userRepository, OrderRecordRepository orderRepository) {
        this.userRepository = userRepository;
        this.orderRepository = orderRepository;
    }

    public OrderRecord createOrder(String username, String email, String itemName, String idCard, String phone,
                                   String paymentCard, String address, String secondaryContact) {
        AppUser user = new AppUser();
        user.setUsername(username);
        user.setEmail(email);
        user.setPhone(phone);
        user.setIdCard(idCard);
        user = userRepository.save(user);

        OrderRecord order = new OrderRecord();
        order.setUser(user);
        order.setItemName(itemName);
        order.setIdCard(idCard);
        order.setPhone(phone);
        order.setPaymentCard(paymentCard);
        order.setAddress(address);
        order.setSecondaryContact(secondaryContact);
        return orderRepository.save(order);
    }

    public OrderDetailDto getOrderDetail(Long orderId) {
        OrderRecord order = orderRepository.findById(orderId).orElseThrow();
        OrderDetailDto dto = new OrderDetailDto();
        dto.orderId = order.getId();
        dto.itemName = order.getItemName();
        dto.userId = order.getUser().getId();
        dto.username = order.getUser().getUsername();
        dto.email = order.getUser().getEmail();
        dto.userPhone = order.getUser().getPhone();
        dto.userIdCard = order.getUser().getIdCard();
        dto.idCard = order.getIdCard();
        dto.phone = order.getPhone();
        dto.paymentCard = order.getPaymentCard();
        dto.address = order.getAddress();
        dto.secondaryContact = order.getSecondaryContact();
        return dto;
    }

    public Page<AppUser> listUsers(int page, int size) {
        return userRepository.findAll(PageRequest.of(page, size));
    }
}
