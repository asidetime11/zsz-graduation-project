# 漏洞说明文件（easy-05）

- 难度级别：easy
- 业务场景：求职简历投递系统
- 主漏洞：Purpose Limitation Violation（将求职数据直接用于营销短信）
- 次要漏洞：
  - Missing Consent（二次用途未征得同意）
  - Sensitive Data Exposure（简历附件 URL 可被猜测）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：email, phone, resume_file, expected_salary
  - 非必要字段：social_account
- 预期接口与页面范围：
  - API：POST /api/resume/submit, POST /api/marketing/push
  - 页面：resume_submit.ejs, marketing_console.ejs
- 预期严重级别分布：
  - critical: 0
  - high: 2（Purpose Limitation Violation, Sensitive Data Exposure）
  - medium: 1（Missing Consent）
- 备注：本批次 easy 主漏洞类别唯一（Purpose Limitation Violation）。
