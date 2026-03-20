# 漏洞说明文件（medium-08）

- 难度级别：medium
- 业务场景：统一身份认证中心
- 主漏洞：JWT Misconfiguration（使用弱密钥且不校验 exp）
- 次要漏洞：
  - Insecure Token Storage（令牌写入可被前端脚本读取的位置）
  - Missing Token Revocation（注销后令牌仍可用）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：user_id, role, jwt_token
  - 非必要字段：theme_preference
- 预期接口与页面范围：
  - API：POST /api/auth/login, GET /api/auth/profile, POST /api/auth/logout
  - 页面：login.ejs, account_center.ejs
- 预期严重级别分布：
  - critical: 1（JWT Misconfiguration）
  - high: 1（Missing Token Revocation）
  - medium: 1（Insecure Token Storage）
- 备注：本批次 medium 主漏洞类别唯一（JWT Misconfiguration）。
