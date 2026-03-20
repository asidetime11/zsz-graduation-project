# vuln_plan_easy_02

- 难度级别：easy
- 业务场景：校园活动报名系统
- 主漏洞：Data Minimization（收集与报名无关的父母职业、年收入）
- 次要漏洞：
  - Missing Consent（报名时未展示隐私同意）
  - Sensitive Data Exposure（联系方式明文入库）
- 关键数据字段：
  - 敏感字段：studentPhone, emergencyPhone
  - 非必要字段：parentJob, annualIncome
- 预期接口与页面范围：
  - POST /events/apply
  - GET /events/applicants
  - 页面：apply_form.html、applicant_list.html
- 预期严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 2（Data Minimization, Missing Consent）
  - medium: 0
- 备注：主漏洞 Data Minimization 为 easy 批次唯一主漏洞
