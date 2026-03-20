# vuln_plan_easy_08

- 难度级别：easy
- 业务场景：意见反馈平台
- 主漏洞：XSS（反馈内容未转义直接渲染）
- 次要漏洞：
  - Missing Consent（无隐私说明与同意）
  - Sensitive Logging（日志记录邮箱和手机号）
- 关键数据字段：
  - 敏感字段：email, phone
  - 非必要字段：company
- 预期接口与页面范围：
  - POST /feedback/submit
  - GET /feedback/list
  - 页面：feedback_form.html、feedback_list.html
- 预期严重级别分布：
  - critical: 0
  - high: 2（XSS, Missing Consent）
  - medium: 1（Sensitive Logging）
- 备注：主漏洞 XSS 为 easy 批次唯一主漏洞
