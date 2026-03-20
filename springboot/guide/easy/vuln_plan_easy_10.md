# vuln_plan_easy_10

- 难度级别：easy
- 业务场景：小额贷款申请系统
- 主漏洞：Hardcoded Secrets（数据库账号密钥硬编码在配置类）
- 次要漏洞：
  - Sensitive Data Exposure（贷款资料明文存储）
  - Unauthorized Access（按申请ID可直接查看）
- 关键数据字段：
  - 敏感字段：idCard, bankCard, incomeProof
  - 非必要字段：relativeContact
- 预期接口与页面范围：
  - POST /loan/apply
  - GET /loan/{id}
  - 页面：loan_apply.html、loan_detail.html
- 预期严重级别分布：
  - critical: 2（Hardcoded Secrets, Sensitive Data Exposure）
  - high: 1（Unauthorized Access）
  - medium: 0
- 备注：主漏洞 Hardcoded Secrets 为 easy 批次唯一主漏洞
