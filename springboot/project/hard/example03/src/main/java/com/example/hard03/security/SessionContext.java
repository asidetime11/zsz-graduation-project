package com.example.hard03.security;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Component;

@Component
public class SessionContext {
    public String currentGroup(HttpServletRequest request) {
        String group = request.getHeader("X-Manager-Group");
        return group == null ? "G-A" : group;
    }
}
