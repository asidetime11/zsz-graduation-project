# 漏洞说明文件（easy-03）

- 难度级别：easy
- 业务场景：二手交易平台用户资料完善
- 主漏洞：Data Minimization Violation（超范围收集“婚姻状态、子女人数、车牌号”）
- 次要漏洞：
  - Missing Retention Policy（无数据保留期限）
  - Logging Sensitive Data（日志打印身份证后 6 位）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：real_name, id_card, bank_account
  - 非必要字段：marital_status, children_count, car_plate
- 预期接口与页面范围：
  - API：PUT /api/profile, GET /api/admin/profiles
  - 页面：profile_edit.ejs, profile_audit.ejs
- 预期严重级别分布：
  - critical: 0
  - high: 1（Data Minimization Violation）
  - medium: 2（Missing Retention Policy, Logging Sensitive Data）
- 备注：本批次 easy 主漏洞类别唯一（Data Minimization Violation）。
