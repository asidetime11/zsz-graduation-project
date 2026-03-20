# 漏洞说明文件（easy-04）

- 难度级别：easy
- 业务场景：社区团购收货地址管理
- 主漏洞：Unrestricted Data Retention（历史地址与电话永久保存且不可删除）
- 次要漏洞：
  - Missing Consent（无“同意历史留存”说明）
  - Export Without Masking（后台导出未脱敏）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：receiver_name, receiver_phone, full_address
  - 非必要字段：address_label_note
- 预期接口与页面范围：
  - API：POST /api/address, DELETE /api/address/:id, GET /api/admin/export-address
  - 页面：address_book.ejs, admin_export.ejs
- 预期严重级别分布：
  - critical: 0
  - high: 2（Unrestricted Data Retention, Export Without Masking）
  - medium: 1（Missing Consent）
- 备注：本批次 easy 主漏洞类别唯一（Unrestricted Data Retention）。
