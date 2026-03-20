# 漏洞说明文件（medium-01）

- 难度级别：medium
- 业务场景：SaaS 客服工单系统
- 主漏洞：Broken Access Control（普通坐席可越权访问主管工单）
- 次要漏洞：
  - Missing Audit Trail（越权访问未审计）
  - Sensitive Data Exposure（工单详情包含明文身份证）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：ticket_id, customer_id_card, customer_phone
  - 非必要字段：customer_family_status
- 预期接口与页面范围：
  - API：GET /api/tickets/:id, PATCH /api/tickets/:id/assign
  - 页面：ticket_detail.ejs, ticket_assign.ejs
- 预期严重级别分布：
  - critical: 1（Broken Access Control）
  - high: 1（Sensitive Data Exposure）
  - medium: 1（Missing Audit Trail）
- 备注：本批次 medium 主漏洞类别唯一（Broken Access Control）。
