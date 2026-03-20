# vuln_plan_easy_04

- 难度级别：easy
- 业务场景：在线简历投递系统
- 主漏洞：Data Over-exposure（候选人列表直接返回证件号和联系方式）
- 次要漏洞：
  - Data Minimization（采集婚育情况）
  - Missing Consent（无授权确认）
- 关键数据字段：
  - 敏感字段：idCard, phone, email
  - 非必要字段：maritalStatus, fertilityPlan
- 预期接口与页面范围：
  - POST /resume/submit
  - GET /resume/candidates
  - 页面：resume_submit.html、candidate_list.html
- 预期严重级别分布：
  - critical: 0
  - high: 3（Data Over-exposure, Data Minimization, Missing Consent）
  - medium: 0
- 备注：主漏洞 Data Over-exposure 为 easy 批次唯一主漏洞
