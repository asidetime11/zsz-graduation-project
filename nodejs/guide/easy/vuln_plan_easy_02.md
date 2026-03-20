# 漏洞说明文件（easy-02）

- 难度级别：easy
- 业务场景：校园活动报名系统
- 主漏洞：Missing Consent（采集个人信息但无任何授权勾选与时间戳）
- 次要漏洞：
  - Sensitive Data Exposure（紧急联系人电话明文存储）
  - Excessive Data Collection（收集“父母工作单位”）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：student_id, phone, emergency_phone
  - 非必要字段：parent_company
- 预期接口与页面范围：
  - API：POST /api/events/signup, GET /api/events/signups
  - 页面：signup.ejs, signup_admin.ejs
- 预期严重级别分布：
  - critical: 0
  - high: 2（Missing Consent, Sensitive Data Exposure）
  - medium: 1（Excessive Data Collection）
- 备注：本批次 easy 主漏洞类别唯一（Missing Consent）。
