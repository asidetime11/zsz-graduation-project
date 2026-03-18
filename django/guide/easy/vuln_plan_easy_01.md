# vuln_plan_easy_01

- 难度级别：easy
- 业务场景：用户注册系统（收集姓名、证件号、手机号、银行卡）
- 主漏洞：Sensitive Data Exposure（身份证号、手机号、银行卡号明文存储，无任何加密）
- 次要漏洞：
  - Data Minimization（收集与注册无关的家庭成员数量字段）
  - Missing Consent（无同意字段，无法追踪用户是否同意数据采集）
- 涉及模型与字段：
  - UserProfile: name, id_card, phone, bank_account, family_members, created_at
- API/页面：
  - POST /register/（用户注册提交）
  - GET /users/（用户列表查询）
  - 页面：注册表单页（register.html）、用户列表页（user_list.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 2（Data Minimization, Missing Consent）
  - medium: 0
- 备注：主漏洞为 Sensitive Data Exposure，本批次唯一，其他项目此类别只能作为次要漏洞出现。
