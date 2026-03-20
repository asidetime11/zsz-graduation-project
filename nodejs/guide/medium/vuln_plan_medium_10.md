# 漏洞说明文件（medium-10）

- 难度级别：medium
- 业务场景：开放平台前后端分离应用
- 主漏洞：Insecure CORS Configuration（允许任意源并携带凭据）
- 次要漏洞：
  - Sensitive Data Exposure（跨站可读取用户资料接口）
  - Missing Origin Validation（白名单机制缺失）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：profile, email, phone, api_key_masked
  - 非必要字段：ui_layout_choice
- 预期接口与页面范围：
  - API：GET /api/me, GET /api/me/orders
  - 页面：dashboard.ejs, openapi_console.ejs
- 预期严重级别分布：
  - critical: 1（Insecure CORS Configuration）
  - high: 1（Sensitive Data Exposure）
  - medium: 1（Missing Origin Validation）
- 备注：本批次 medium 主漏洞类别唯一（Insecure CORS Configuration）。
