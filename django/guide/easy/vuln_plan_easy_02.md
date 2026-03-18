# vuln_plan_easy_02

- 难度级别：easy
- 业务场景：简历投递系统（求职者提交个人简历）
- 主漏洞：Data Minimization（收集婚姻状况、宗教信仰、病史等与招聘业务无关的字段）
- 次要漏洞：
  - Sensitive Data Exposure（身份证号明文存储）
  - Data Over-exposure（简历列表接口返回全部字段含敏感信息）
- 涉及模型与字段：
  - CandidateProfile: name, email, id_card, phone, marital_status, religion, medical_history, created_at
- API/页面：
  - POST /resume/submit/（简历提交）
  - GET /resumes/（简历列表）
  - 页面：简历提交表单页（submit.html）、简历列表页（resume_list.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure - id_card 明文）
  - high: 2（Data Minimization, Data Over-exposure）
  - medium: 0
- 备注：主漏洞为 Data Minimization，本批次唯一。
