package com.example.hard04.security;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Component;

@Component
public class SessionContext {
    public String currentDept(HttpServletRequest request) {
        String dept = request.getHeader("X-Dept");
        return dept == null ? "service-center" : dept;
    }
}
