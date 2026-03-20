# vuln_plan_easy_09

- 难度级别：easy
- 业务场景：客服工单系统
- 主漏洞：Sensitive Logging（日志打印身份证、手机号、地址）
- 次要漏洞：
  - Data Minimization（收集与工单无关的家庭住址）
  - Missing Consent（无日志告知与同意）
- 关键数据字段：
  - 敏感字段：idCard, phone, address
  - 非必要字段：familyAddress
- 预期接口与页面范围：
  - POST /tickets/create
  - GET /tickets
  - 页面：ticket_form.html、ticket_list.html
- 预期严重级别分布：
  - critical: 0
  - high: 3（Sensitive Logging, Data Minimization, Missing Consent）
  - medium: 0
- 备注：主漏洞 Sensitive Logging 为 easy 批次唯一主漏洞
