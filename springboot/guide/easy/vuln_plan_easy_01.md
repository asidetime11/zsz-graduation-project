# vuln_plan_easy_01

- 难度级别：easy
- 业务场景：用户注册系统（收集姓名、证件号、手机号、银行卡）
- 主漏洞：Sensitive Data Exposure（身份证号、手机号、银行卡号明文存储）
- 次要漏洞：
  - Data Minimization（收集与注册无关的家庭成员数量）
  - Missing Consent（无同意字段，无法追踪授权）
- 关键数据字段：
  - 敏感字段：idCard, phone, bankAccount
  - 非必要字段：familyMembers
- 预期接口与页面范围：
  - POST /register
  - GET /users
  - 页面：register.html、user_list.html
- 预期严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 2（Data Minimization, Missing Consent）
  - medium: 0
- 备注：主漏洞 Sensitive Data Exposure 为 easy 批次唯一主漏洞
