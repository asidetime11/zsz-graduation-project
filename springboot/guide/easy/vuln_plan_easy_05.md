# vuln_plan_easy_05

- 难度级别：easy
- 业务场景：员工信息查询系统
- 主漏洞：Unauthorized Access（按员工ID查询详情，无归属校验）
- 次要漏洞：
  - Data Over-exposure（详情返回薪资与银行卡）
  - Sensitive Logging（日志打印完整身份证号）
- 关键数据字段：
  - 敏感字段：idCard, salary, bankAccount
  - 非必要字段：familyAddress
- 预期接口与页面范围：
  - GET /employees/{id}
  - GET /employees
  - 页面：employee_detail.html、employee_list.html
- 预期严重级别分布：
  - critical: 1（Unauthorized Access）
  - high: 2（Data Over-exposure, Sensitive Logging）
  - medium: 0
- 备注：主漏洞 Unauthorized Access 为 easy 批次唯一主漏洞
