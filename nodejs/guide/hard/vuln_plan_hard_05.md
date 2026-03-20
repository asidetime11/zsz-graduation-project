# 漏洞说明文件（hard-05）

- 难度级别：hard
- 业务场景：多租户 CRM 平台
- 主漏洞：Tenant Isolation Failure（租户边界失效导致跨租户读取客户数据）
- 次要漏洞：
  - Broken Object Scoping（查询条件缺失 tenant_id）
  - Export Without Authorization（导出接口无租户校验）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：tenant_id, customer_phone, customer_contract
  - 非必要字段：customer_tag_color
- 预期接口与页面范围：
  - API：GET /api/tenants/:tid/customers, GET /api/customers/export
  - 页面：tenant_customers.ejs, export_center.ejs
- 预期严重级别分布：
  - critical: 1（Tenant Isolation Failure）
  - high: 2（Broken Object Scoping, Export Without Authorization）
  - medium: 0
- 备注：本批次 hard 主漏洞类别唯一（Tenant Isolation Failure）。
