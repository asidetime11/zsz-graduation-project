# vuln_plan_easy_04

- 难度级别：easy
- 业务场景：新闻邮件订阅系统（用户提交邮箱和手机号订阅新闻推送）
- 主漏洞：Missing Consent（收集用户邮箱、手机号、出生日期时无同意字段，无法追踪授权记录）
- 次要漏洞：
  - Sensitive Data Exposure（手机号明文存储）
  - Data Minimization（额外收集出生日期、家庭住址等与订阅无关的字段）
- 涉及模型与字段：
  - Subscriber: name, email, phone, birth_date, address, created_at
- API/页面：
  - POST /subscribe/（提交订阅）
  - GET /subscribers/（订阅者列表）
  - 页面：订阅表单页（subscribe.html）、订阅者列表页（subscriber_list.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure - phone 明文）
  - high: 2（Missing Consent, Data Minimization）
  - medium: 0
- 备注：主漏洞为 Missing Consent，本批次唯一。
