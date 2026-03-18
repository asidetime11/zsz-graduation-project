# vuln_plan_easy_10

- 难度级别：easy
- 业务场景：访客登记系统（访客填写信息登记进出，后台可查看访客列表）
- 主漏洞：Hardcoded Secrets（第三方通知服务 API 密钥硬编码在 views.py 中，同时 SECRET_KEY 使用默认弱值）
- 次要漏洞：
  - Sensitive Data Exposure（访客身份证号、手机号明文存储）
  - Data Over-exposure（访客列表接口返回全部字段含证件信息）
- 涉及模型与字段：
  - VisitorLog: name, id_card, phone, company, visit_reason, host_name, visit_time
- API/页面：
  - POST /visitor/register/（访客登记，代码内硬编码通知 API 密钥）
  - GET /visitors/（访客列表，返回所有字段）
  - 页面：访客登记页（register.html）、访客列表页（visitor_list.html）
- 严重级别分布：
  - critical: 2（Hardcoded Secrets, Sensitive Data Exposure）
  - high: 1（Data Over-exposure）
  - medium: 0
- 备注：主漏洞为 Hardcoded Secrets，本批次唯一。
