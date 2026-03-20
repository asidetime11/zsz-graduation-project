package com.example.hard02.security;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Component;

@Component
public class SessionContext {
    public String currentDept(HttpServletRequest request) {
        return request.getHeader("X-Dept");
    }
}
