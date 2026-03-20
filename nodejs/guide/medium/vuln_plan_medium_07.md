# 漏洞说明文件（medium-07）

- 难度级别：medium
- 业务场景：短信验证码登录
- 主漏洞：Missing Rate Limiting on OTP/Login（验证码与登录接口可被暴力尝试）
- 次要漏洞：
  - Weak OTP Expiry（验证码有效期过长）
  - Account Enumeration（返回“手机号不存在”可枚举账户）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：phone, otp_code, login_token
  - 非必要字段：referrer_phone
- 预期接口与页面范围：
  - API：POST /api/auth/send-otp, POST /api/auth/otp-login
  - 页面：otp_login.ejs
- 预期严重级别分布：
  - critical: 0
  - high: 2（Missing Rate Limiting on OTP/Login, Account Enumeration）
  - medium: 1（Weak OTP Expiry）
- 备注：本批次 medium 主漏洞类别唯一（Missing Rate Limiting on OTP/Login）。
