package com.example.hard01.security;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Component;

@Component
public class SessionContext {
    public Long currentDoctorId(HttpServletRequest request) {
        String id = request.getHeader("X-Doctor-Id");
        if (id == null || id.isBlank()) {
            return 1L;
        }
        return Long.parseLong(id);
    }
}
