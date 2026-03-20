# 漏洞说明文件（hard-08）

- 难度级别：hard
- 业务场景：Node.js + MongoDB 用户检索服务
- 主漏洞：NoSQL Injection Chain（查询条件可注入 $ne/$regex 进而绕过认证）
- 次要漏洞：
  - Insecure Query Builder（将用户输入直接合并查询对象）
  - Account Enumeration（响应差异暴露账号存在性）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：username, password_hash, phone, reset_token
  - 非必要字段：nickname_style
- 预期接口与页面范围：
  - API：POST /api/auth/login, GET /api/users/search
  - 页面：login.ejs, user_search.ejs
- 预期严重级别分布：
  - critical: 1（NoSQL Injection Chain）
  - high: 1（Insecure Query Builder）
  - medium: 1（Account Enumeration）
- 备注：本批次 hard 主漏洞类别唯一（NoSQL Injection Chain）。
