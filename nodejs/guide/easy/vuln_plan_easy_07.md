# 漏洞说明文件（easy-07）

- 难度级别：easy
- 业务场景：线上报修工单系统
- 主漏洞：Logging Sensitive Data（服务端日志输出姓名+手机号+住址全量内容）
- 次要漏洞：
  - Unrestricted Data Retention（日志长期不清理）
  - Data Minimization（报修单收集身份证正反面）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：name, phone, address, id_card_images
  - 非必要字段：household_register_city
- 预期接口与页面范围：
  - API：POST /api/tickets, GET /api/admin/tickets
  - 页面：ticket_create.ejs, ticket_list.ejs
- 预期严重级别分布：
  - critical: 0
  - high: 2（Logging Sensitive Data, Unrestricted Data Retention）
  - medium: 1（Data Minimization）
- 备注：本批次 easy 主漏洞类别唯一（Logging Sensitive Data）。
