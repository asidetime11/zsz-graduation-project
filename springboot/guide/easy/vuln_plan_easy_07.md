# vuln_plan_easy_07

- 难度级别：easy
- 业务场景：客户检索后台
- 主漏洞：SQL Injection（关键字拼接到查询语句）
- 次要漏洞：
  - Data Over-exposure（搜索结果包含全部字段）
  - Sensitive Logging（记录原始查询参数）
- 关键数据字段：
  - 敏感字段：idCard, phone, bankAccount
  - 非必要字段：remark
- 预期接口与页面范围：
  - GET /customers/search?kw=
  - GET /customers
  - 页面：customer_search.html、customer_list.html
- 预期严重级别分布：
  - critical: 1（SQL Injection）
  - high: 2（Data Over-exposure, Sensitive Logging）
  - medium: 0
- 备注：主漏洞 SQL Injection 为 easy 批次唯一主漏洞
