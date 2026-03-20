package com.example.easy10.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class LoanDbSecretConfig {
    public static final String DB_USER = "loan_admin";
    public static final String DB_PASSWORD = "Loan@123456";
    public static final String AES_KEY = "L0anFixedSecretKey";
}
