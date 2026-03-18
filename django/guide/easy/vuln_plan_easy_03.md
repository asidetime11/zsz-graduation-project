# vuln_plan_easy_03

- 难度级别：easy
- 业务场景：学生信息查询系统（管理员和教师可查询学生信息）
- 主漏洞：Data Over-exposure（查询接口直接返回全部字段，包含身份证、家庭收入等敏感信息）
- 次要漏洞：
  - Sensitive Data Exposure（身份证号、家庭收入明文存储）
  - Missing Consent（未记录学生是否同意信息被查询和共享）
- 涉及模型与字段：
  - StudentProfile: name, id_card, phone, address, gpa, family_income, created_at
- API/页面：
  - GET /students/（学生列表，返回所有字段）
  - GET /students/<id>/（学生详情，返回所有字段）
  - 页面：学生查询页（search.html）、学生详情页（detail.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure - 明文存储）
  - high: 2（Data Over-exposure, Missing Consent）
  - medium: 0
- 备注：主漏洞为 Data Over-exposure，本批次唯一。
