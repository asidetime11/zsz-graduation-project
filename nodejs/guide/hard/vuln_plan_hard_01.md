# 漏洞说明文件（hard-01）

- 难度级别：hard
- 业务场景：可配置规则引擎的风控平台
- 主漏洞：Prototype Pollution to Privilege Escalation（污染对象原型导致权限字段被提升）
- 次要漏洞：
  - Broken Access Control（管理接口权限判断受污染影响）
  - Insufficient Input Validation（深层 JSON 未过滤）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：role, permission_set, risk_score
  - 非必要字段：profile_badge
- 预期接口与页面范围：
  - API：POST /api/rules/preview, POST /api/rules/save
  - 页面：rule_builder.ejs, admin_policy.ejs
- 预期严重级别分布：
  - critical: 1（Prototype Pollution to Privilege Escalation）
  - high: 2（Broken Access Control, Insufficient Input Validation）
  - medium: 0
- 备注：本批次 hard 主漏洞类别唯一（Prototype Pollution to Privilege Escalation）。
