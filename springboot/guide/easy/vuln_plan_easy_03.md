# vuln_plan_easy_03

- 难度级别：easy
- 业务场景：医疗预约登记系统
- 主漏洞：Missing Consent（无隐私授权勾选与授权记录）
- 次要漏洞：
  - Sensitive Data Exposure（病史与身份证号明文存储）
  - Data Over-exposure（列表页返回全部患者字段）
- 关键数据字段：
  - 敏感字段：idCard, medicalHistory, phone
  - 非必要字段：occupation
- 预期接口与页面范围：
  - POST /appointments/book
  - GET /patients
  - 页面：appointment_form.html、patient_list.html
- 预期严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 2（Missing Consent, Data Over-exposure）
  - medium: 0
- 备注：主漏洞 Missing Consent 为 easy 批次唯一主漏洞
