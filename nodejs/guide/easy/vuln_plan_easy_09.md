# 漏洞说明文件（easy-09）

- 难度级别：easy
- 业务场景：企业内部通讯录导出
- 主漏洞：Export Without Authorization（任意普通用户可导出全员通讯录）
- 次要漏洞：
  - Export Without Masking（导出文件不脱敏）
  - Missing Audit Trail（无导出审计记录）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：employee_no, name, mobile, email
  - 非必要字段：personal_wechat
- 预期接口与页面范围：
  - API：GET /api/contacts/export, GET /api/contacts
  - 页面：contacts.ejs, export_history.ejs
- 预期严重级别分布：
  - critical: 1（Export Without Authorization）
  - high: 1（Export Without Masking）
  - medium: 1（Missing Audit Trail）
- 备注：本批次 easy 主漏洞类别唯一（Export Without Authorization）。
