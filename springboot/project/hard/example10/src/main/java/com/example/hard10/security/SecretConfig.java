package com.example.hard10.security;

import org.springframework.stereotype.Component;

@Component
public class SecretConfig {
    public static final String JWT_SECRET = "jwt-prod-super-secret-2026";
    public static final String DB_PASSWORD = "credit_db_password_@123";
    public static final String OSS_ACCESS_KEY = "oss_ak_2026_xxx";
    public static final String OSS_SECRET_KEY = "oss_sk_2026_xxx";
}
