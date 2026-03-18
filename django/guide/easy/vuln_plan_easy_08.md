# vuln_plan_easy_08

- 难度级别：easy
- 业务场景：客服工单系统（用户提交工单，系统记录并展示工单列表）
- 主漏洞：Sensitive Logging（工单创建时使用 logging.info 打印完整请求体，包含身份证号、手机号等敏感字段）
- 次要漏洞：
  - Sensitive Data Exposure（身份证号明文存储在工单记录中）
  - Data Over-exposure（工单列表接口返回全部字段含敏感信息）
- 涉及模型与字段：
  - SupportTicket: name, id_card, phone, email, ticket_content, status, created_at
- API/页面：
  - POST /ticket/create/（创建工单，触发敏感日志）
  - GET /tickets/（工单列表，返回所有字段）
  - 页面：工单提交页（create_ticket.html）、工单列表页（ticket_list.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 2（Sensitive Logging, Data Over-exposure）
  - medium: 0
- 备注：主漏洞为 Sensitive Logging，本批次唯一。
