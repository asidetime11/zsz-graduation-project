# 漏洞说明文件（easy-01）

- 难度级别：easy
- 业务场景：在线问诊预约平台注册流程
- 主漏洞：Sensitive Data Exposure（身份证号、手机号、医保卡号明文存储）
- 次要漏洞：
  - Data Minimization（额外收集“家庭年收入”与“宗教信仰”）
  - Missing Consent（未记录隐私政策同意状态）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：id_card, phone, medical_insurance_no, emergency_contact
  - 非必要字段：family_income, religion
- 预期接口与页面范围：
  - API：POST /api/register, GET /api/patients
  - 页面：register.ejs, patient_list.ejs
- 预期严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 2（Data Minimization, Missing Consent）
  - medium: 0
- 备注：本批次 easy 主漏洞类别唯一（Sensitive Data Exposure）。
