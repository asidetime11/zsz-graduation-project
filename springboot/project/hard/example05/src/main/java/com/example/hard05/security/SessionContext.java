package com.example.hard05.security;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Component;

@Component
public class SessionContext {
    public String currentInstitution(HttpServletRequest request) {
        String ins = request.getHeader("X-Institution-Code");
        return ins == null ? "INST-A" : ins;
    }
}
