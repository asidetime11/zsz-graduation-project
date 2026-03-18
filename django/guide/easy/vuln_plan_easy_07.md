# vuln_plan_easy_07

- 难度级别：easy
- 业务场景：意见反馈系统（用户提交文字反馈，管理员页面展示反馈列表）
- 主漏洞：XSS（反馈内容未过滤，通过 mark_safe 或模板 |safe 直接渲染到管理员列表页，存在存储型 XSS）
- 次要漏洞：
  - Sensitive Data Exposure（联系人手机号、邮箱明文存储）
  - Missing Consent（收集联系方式时无同意字段）
- 涉及模型与字段：
  - Feedback: name, email, phone, feedback_content, created_at
- API/页面：
  - POST /feedback/（提交反馈）
  - GET /feedbacks/（反馈列表，使用 |safe 渲染 feedback_content）
  - 页面：反馈提交页（feedback.html）、反馈列表页（feedback_list.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 2（XSS, Missing Consent）
  - medium: 0
- 备注：主漏洞为 XSS，本批次唯一。
