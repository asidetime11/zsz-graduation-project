# 漏洞说明文件（easy-08）

- 难度级别：easy
- 业务场景：教育平台账户注册与登录
- 主漏洞：Weak Credential Storage（密码明文或可逆加密存储）
- 次要漏洞：
  - Missing Rate Limit（登录接口无频率限制）
  - Sensitive Data Exposure（找回密码接口返回完整邮箱）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：email, password, phone
  - 非必要字段：study_goal_detail
- 预期接口与页面范围：
  - API：POST /api/auth/register, POST /api/auth/login, POST /api/auth/reset
  - 页面：register.ejs, login.ejs, reset_password.ejs
- 预期严重级别分布：
  - critical: 1（Weak Credential Storage）
  - high: 1（Sensitive Data Exposure）
  - medium: 1（Missing Rate Limit）
- 备注：本批次 easy 主漏洞类别唯一（Weak Credential Storage）。
